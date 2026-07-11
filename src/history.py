import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "history.db"
print("Database path:", DB_PATH)

def initialize_database():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        tweet TEXT,
        sentiment TEXT,
        risk_level TEXT,
        risk_score INTEGER
    )
    """)

    conn.commit()
    conn.close()


initialize_database()


def save_prediction(tweet, result):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    now = datetime.now()

    cursor.execute("""
    INSERT INTO predictions
    (date,time,tweet,sentiment,risk_level,risk_score)
    VALUES (?,?,?,?,?,?)
    """, (
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        tweet,
        result["sentiment"],
        result["risk_level"],
        result["risk_score"]
    ))

    conn.commit()
    conn.close()


def load_history():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM predictions ORDER BY id DESC",
        conn
    )

    conn.close()

    return df