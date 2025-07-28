import sqlite3

DB_PATH = 'school.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS student(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER   
                )
                """)
    conn.commit()
    conn.close()