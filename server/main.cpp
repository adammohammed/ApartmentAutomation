#include "temperature_module.h"

int main(int argc, char * argv[])
{
  mqtt_tempmod *tempmod;
  int rc;

  mosqpp::lib_init();

  tempmod = new mqtt_tempmod("tempmod","localhost", 1883);

  while(1){
    rc = tempmod->loop();
    if (rc){
      tempmod->reconnect();
    }
  }


  mosqpp::lib_cleanup();

  return 0;
}
