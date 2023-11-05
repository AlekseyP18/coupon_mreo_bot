from dataclasses import dataclass
import sqlite3
from sqlite3 import Connection


@dataclass
class APIsettings:
    _gid: str
    _gat: str
    _ga_3GVV2WPF7F: str
    WEBCHSID2: str
    _csrf: str
    X_CSRF_Token: str


def create_database_table_if_not_exists() -> Connection:
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            user_id INTEGER PRIMARY KEY
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS APIsettings (
            _gid TEXT,
            _gat TEXT,
            _ga_3GVV2WPF7F TEXT,
            WEBCHSID2 TEXT,
            _csrf TEXT,
            X_CSRF_Token TEXT
        )
    ''')
    conn.commit()
    return conn


def get_last_settings() -> APIsettings:
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    settings = cursor.execute('''
        SELECT * from APIsettings LIMIT(1)
    ''').fetchone()
    return APIsettings(*settings)


def set_last_settings(settings: APIsettings):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO APIsettings (_gid, _gat, _ga_3GVV2WPF7F, WEBCHSID2, _csrf, X_CSRF_Token) VALUES(?, ?, ?, ?, ?, ?)
    ''', (settings._gid, settings._gat, settings._ga_3GVV2WPF7F,
          settings.WEBCHSID2, settings._csrf, settings.X_CSRF_Token))
    conn.commit()