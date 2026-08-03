import time
from smbus2 import SMBus, i2c_msg
import sqlite3
from datetime import datetime

AM2320_ADDR = 0x5C

def read_am2320():
    try:
        with SMBus(1) as bus:
            try:
                bus.write_quick(AM2320_ADDR)
            except OSError:
                pass

            time.sleep(0.0035)

            cmd = [0x03, 0x00, 0x04]
            bus.write_i2c_block_data(AM2320_ADDR, cmd[0], cmd[1:])
            time.sleep(0.003)

            read_msg = i2c_msg.read(AM2320_ADDR, 6)
            bus.i2c_rdwr(read_msg)
            data = list(read_msg)

            if len(data) < 6 or data[0] != 0x03 or data[1] != 0x04:
                return None

            humidity = (data[2] << 8 | data[3]) / 10.0
            raw_temp = data[4] << 8 | data[5]

            if raw_temp & 0x8000:
                temperature = -(raw_temp & 0x7FFF) / 10.0
            else:
                temperature = raw_temp / 10.0

            return {"temperature": temperature, "humidity": humidity}

    except (OSError, IndexError, ValueError):
        return None

if __name__ == "__main__":
    try:
        while True:
            result = None
            while result is None:
                result = read_am2320()
            
            temp = (result['temperature'])
            hum = (result['humidity'])
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            conn = sqlite3.connect('sensor_data.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO measurements (timestamp, temperature, humidity) VALUES (?, ?, ?)", 
                (now, temp, hum)
            )
            conn.commit()
            conn.close()
            print(f"{temp}°C, {hum}%")

            time.sleep(15)

    except KeyboardInterrupt:
        print("\nProgram został zatrzymany.")
