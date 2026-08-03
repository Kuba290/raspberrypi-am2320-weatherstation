from flask import Flask, render_template, jsonify, request
import sqlite3

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

@app.route('/')
def index():
    return render_template('index.html')

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