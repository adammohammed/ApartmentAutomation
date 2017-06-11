# Home automation
This is software to accept data from MQTT channels and provide a visualization
to a website of the trend of the data. The program uses SQLite3 and d3.js to
create dynamic visuals on the website.

The sensor setup I am using is DS1820B and an ESP8266 ESP-01S. The
microcontroller and sensor are in a room and are measuring the temperature every
10 minutes and attempting to publish to the MQTT server.

## Roadmap
+ DONE: Read Temperatures from room using ESP8266 and DS1820B Sensor
+ DONE: Send Temperatures to MQTT server
+ DONE: Read Temperatures from MQTT topic
+ DONE: Store into Database along with time stamp
+ DONE: Visualize Data on website
+ DONE: Refresh website periodically with new data, sliding window
+ TODO: Set High and Low Alarm Temperatures
+ TODO: Modify Mechanical Thermostat to turn heat/AC on or off.
+ TODO: Create a setup procedure/scripts to make it easy to use.
