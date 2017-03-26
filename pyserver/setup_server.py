import os

import sqlite3

def create_tables():
    ''' Creates all tables needed to run application'''
    dir = os.getcwd()
    filename = os.path.join(dir,'../db/temperature.db')

    conn = sqlite3.connect(filename)

    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS temperature_log (
    _ID        INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
    LOGGED     DATETIME                              DEFAULT (datetime('now','localtime')),
    CELSIUS    DOUBLE                                NOT NULL
    );
    ''')

    c.execute('''INSERT INTO temperature_log (CELSIUS) VALUES (33.4);''')

    conn.commit()

    conn.close()



if __name__ == "__main__":
    print("Creating Tables")
    create_tables()
    print("Tables Created and entry logged")
