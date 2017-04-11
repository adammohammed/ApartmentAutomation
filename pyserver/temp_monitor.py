import paho.mqtt.client as mqtt
import sqlite3

def on_connect(client, userdata, flags, rc):
    '''
    Connection callback for MQTT
    '''
    print('Connected with resultcode {}'.format(rc))

    client.subscribe('room/temperature_center')


def on_message(client, userdata, message):
    '''
    Message callback for MQTT
    Reads message and stores temp to db
    '''
    data = (float(message.payload),)
    print('{} {}'.format(message.topic, data))
    dbpath = "../db/temperature.db"

    record_temperature(dbpath, data)


def record_temperature(dbfile, temperature_data):
    '''
    Create a new entry to the temperature talbe
    @param conn: Connection object
    @param temperature_data: data from mqtt
    '''
    sql = ''' INSERT INTO temperature_log (TEMPF)
              VALUES (?);'''

    try:
        with sqlite3.connect(dbfile) as conn:
            conn.execute(sql, temperature_data)
    except sqlite3.IntegrityError:
        print("Error occured in INSERT")
    return


if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message


    with open('config.yaml', 'r') as f:
        credentials = yaml.load(f)

    user = credentials['user']
    password = credentials['password']
    client.username_pw_set(user, password)
    client.connect("localhost", 1883, 60)

    client.loop_forever()
