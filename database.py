import sqlite3
from datetime import datetime

#create connection and table if not exists
def init_db():
    conn = sqlite3.connect('health_prediction.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_name TEXT,

            disease TEXT,

            result TEXT,

            risk_percent REAL,

            risk_level TEXT,

            date_time TEXT
        )
    """)

    conn.commit()
    conn.close()

    #function to save prediction result to database
def save_prediction(patient_name, disease, result, risk_percent, risk_level):
    conn = sqlite3.connect('health_prediction.db')
    cursor = conn.cursor()

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO predictions (patient_name, disease, result, risk_percent, risk_level, date_time)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (patient_name, disease, result, risk_percent, risk_level, date_time))

    conn.commit()
    conn.close()
       