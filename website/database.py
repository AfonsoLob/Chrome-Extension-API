import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
import json

DB_STRING = "database.db"

db_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(db_directory, DB_STRING)

def setup_database():
    user_table = """ CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );"""

    with sqlite3.connect(db_path) as con:
        con.execute(user_table)

def cleanup_database():
    users_table = "DROP TABLE IF EXISTS users;"
    with sqlite3.connect(db_path) as con:
        con.execute(users_table)

def add_user(email, password):
    with sqlite3.connect(db_path) as con:
        con.execute("""
        INSERT INTO users (email, password)
        VALUES (?, ?);
        """, (email, generate_password_hash(password)))

def get_user_password(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT password FROM users
        WHERE email = ?;
        """, (email,))
        user_password = cur.fetchall()[0]        
        return user_password[0]
    
def verify_user(user_email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
            SELECT email FROM users;
        """)
        list_of_emails = cur.fetchall()
        for email in list_of_emails:
            email = email[0]
            if (email == user_email): 
                return True
        return False
    
def get_id(email):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id FROM users
        WHERE email = ?;
        """, (email,))
        id = cur.fetchall()[0]
        return id[0]