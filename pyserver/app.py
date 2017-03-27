import json

from flask import Flask
import sqlite3


app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('graph.html')

@app.route('/drawgraph.js')
def js():
    return app.send_static_file('drawgraph.js')

@app.route('/api/temp_sensor')
def get_temps():
    conn = sqlite3.connect('../db/temperature.db')

    c = conn.cursor()
    c.execute('''SELECT * FROM temperature_log order by _ID DESC LIMIT 10;''')

    temps = []

    entries = c.fetchall()
    conn.close()
    for entry in entries:
        t = {'_ID': entry[0],
             'LOGGED': entry[1],
             'TEMPF': entry[2]}
        temps.append(t)

    return json.dumps(temps)



if __name__ == "__main__":
    app.run('127.0.0.1',5000,True)
