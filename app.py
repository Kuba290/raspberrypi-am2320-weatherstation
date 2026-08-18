from flask import Flask, render_template, jsonify, request
import sqlite3
import requests
import location

app = Flask(__name__)

def get_history(limit=50):
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT timestamp, temperature, humidity FROM measurements ORDER BY id DESC LIMIT ?", 
        (limit,)
    )
    data = cursor.fetchall()
    conn.close()
    return data[::-1]

def get_weather():
    latitude = location.latitude
    longitude = location.longitude

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,weather_code&models=ecmwf_ifs&current=temperature_2m,relative_humidity_2m,precipitation,weather_code&timezone=auto&forecast_hours=240&past_hours=0&daily=sunrise,sunset,weather_code,temperature_2m_min,temperature_2m_max,precipitation_sum,moonrise,moonset,moon_phase&forecast_days=7"
    data = requests.get(weather_url).json()

    hourly_forecast = []
    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    humidity = data["hourly"]["relative_humidity_2m"]
    precipitation_prob = data["hourly"]["precipitation_probability"]
    precipitation = data["hourly"]["precipitation"]
    weather_code = data["hourly"]["weather_code"]

    for i in range(len(times)):
        hourly_forecast.append({
            "time": times[i].replace("T", " "),
            "temp": temps[i],
            "humidity": humidity[i],
            "precipitation_prob": precipitation_prob[i],
            "precipitation": precipitation[i],
            "weather_code": weather_code[i]
        })

    daily_forecast = []
    times = [item.split("T")[0] for item in data["daily"]["time"]]
    sunrise = [item.split("T")[1] for item in data["daily"]["sunrise"]]
    sunset = [item.split("T")[1] for item in data["daily"]["sunset"]]
    temps_high = [round(item) for item in data["daily"]["temperature_2m_max"]] 
    temps_low = [round(item) for item in data["daily"]["temperature_2m_min"]]
    weather_code = data["daily"]["weather_code"]
    precipitation_sum = data["daily"]["precipitation_sum"]
    moonrise = [item.split("T")[1] if item and "T" in item else "--:--" for item in data["daily"]["moonrise"]]
    moonset = [item.split("T")[1] if item and "T" in item else "--:--" for item in data["daily"]["moonset"]]
    moon_phase = data["daily"]["moon_phase"]

    for i in range(len(times)):
        daily_forecast.append({
            "time": times[i],
            "sunrise": sunrise[i],
            "sunset": sunset[i],
            "temps_high": temps_high[i],
            "temps_low": temps_low[i],
            "weather_code": weather_code[i],
            "precipitation_sum": precipitation_sum[i],
            "moonrise": moonrise[i],
            "moonset": moonset[i],
            "moon_phase": moon_phase[i]
        })

    current_weather = {
        "temp": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "precipitation": data["current"]["precipitation"],
        "weather_code": data["current"]["weather_code"]
    }

    return current_weather, hourly_forecast, daily_forecast


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    current, forecast, daily = get_weather()
    return render_template('weather.html', current = current, forecast = forecast, daily = daily)

@app.route('/api/data')
def api_data():
    limit = request.args.get('limit', default=50, type=int)
    
    raw_data = get_history(limit)
    
    if not raw_data:
        return jsonify({'labels': [], 'temperatures': [], 'humidities': [], 'current': {'temp': '--', 'hum': '--', 'time': '--'}})

    timestamps = [row[0] for row in raw_data]
    temps = [row[1] for row in raw_data]
    hums = [row[2] for row in raw_data]
    
    current_temp = temps[-1]
    current_hum = hums[-1]
    current_time = timestamps[-1]

    return jsonify({
        'labels': timestamps,
        'temperatures': temps,
        'humidities': hums,
        'current': {
            'temp': current_temp,
            'hum': current_hum,
            'time': current_time
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)