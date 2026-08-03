import sqlite3

conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS measurements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperature REAL,
        humidity REAL
    )
''')

conn.commit()
conn.close()
print("Baza danych utworzona pomyślnie.")