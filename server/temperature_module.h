#ifndef TEMPERATURE_MODULE_H
#define TEMPERATURE_MODULE_H

#include <mosquittopp.h>

class mqtt_tempmod : public mosqpp::mosquittopp
{
 public:
  mqtt_tempmod(const char *id, const char *host, int port);
  ~mqtt_tempmod();

  void on_connect(int rc);
  void on_message(const struct mosquitto_message *message);
  void on_subscribe(int mid, int qos_count, const int *granted_qos);
};

#endif
