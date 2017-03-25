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
    print('{} {}'.format(message.topic, message.payload))
    data = (float(message.payload),)
    dbpath = "../db/temperature.db"

    record_temperature(dbpath, data)


def record_temperature(dbfile, temperature_data):
    '''
    Create a new entry to the temperature talbe
    @param conn: Connection object
    @param temperature_data: data from mqtt
    '''
    sql = ''' INSERT INTO TEMPERATURE_LOG (CELSIUS)
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


    client.connect("localhost", 1883, 60)

    client.loop_forever()
