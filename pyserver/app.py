import json

from flask import Flask, request
import sqlite3


app = Flask(__name__)

water_valve = "closed"

@app.route('/valve_status', methods=["GET"])
def get_water_status():
    out = { "status": water_valve }
    return json.dumps(out)

@app.route('/water', methods=["POST"])
def set_valve_status():
    body = request.get_json();
    if body:
        status = body.get("status", "none")
        global water_valve
        water_valve = status
        return water_valve
    else:
        return "Error: No data (or wrong type)"
    
    
	
@app.route('/debug')
def get_temps_dummy():
    temps = []
    temps.append({'_ID':1, 'LOGGED':'123','TEMPF':'72.0'})
    temps.append({'_ID':2, 'LOGGED':'123','TEMPF':'72.0'})
    temps.append({'_ID':3, 'LOGGED':'123','TEMPF':'72.0'})
    temps.append({'_ID':4, 'LOGGED':'123','TEMPF':'72.0'})

    return json.dumps(temps)

@app.route('/temp_sensor')
def get_temps():
    conn = sqlite3.connect('../db/temperature.db')

    c = conn.cursor()
    c.execute('''SELECT * FROM temperature_log order by _ID DESC LIMIT 30;''')

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
