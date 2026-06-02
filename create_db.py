import sqlite3

conn = sqlite3.connect("database/interview.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    resume_name TEXT,
    ats_score INTEGER,
    skills TEXT,
    resume_text TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS interviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question TEXT,
    answer TEXT,
    feedback TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")