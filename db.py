import sqlite3
from sqlite3 import Connection


def create_database_table_if_not_exists() -> Connection:
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            user_id INTEGER PRIMARY KEY
        )
    ''')
    conn.commit()
    return conn
