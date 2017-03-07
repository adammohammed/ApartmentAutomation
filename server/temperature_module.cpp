#include <cstdio>
#include <cstring>

#include "temperature_module.h"
#include "sqlite_logger.h"

#include <mosquittopp.h>

mqtt_tempmod::mqtt_tempmod(const char *id, const char *host, int port): mosquittopp(id)
{
  int keepalive = 60;
  connect(host,port, keepalive);

};

mqtt_tempmod::~mqtt_tempmod(){

}

void mqtt_tempmod::on_connect(int rc)
{
  printf("Connected with code %d. \n", rc);
  if (rc ==0){
    subscribe(NULL, "room/temperature_center");
  }
}

void mqtt_tempmod::on_message(const struct mosquitto_message *message)
{
	double temp_celsius, temp_farenheit;
	char buf[51];

	if(!strcmp(message->topic, "room/temperature_center")){
		memset(buf, 0, 51*sizeof(char));
		/* Copy N-1 bytes to ensure always 0 terminated. */
		memcpy(buf, message->payload, 50*sizeof(char));
		temp_celsius = atof(buf);
		temp_farenheit = temp_celsius*9.0/5.0 + 32.0;
		snprintf(buf, 50, "%f", temp_farenheit);
        printf("Current Temperature is %3.2f.\n", temp_celsius);
		//publish(NULL, "temperature/farenheit", strlen(buf), buf);
	}
}


void mqtt_tempmod::on_subscribe(int mid, int qos_count, const int *granted_qos)
{
  printf("Subscription succeded.\n");
}
