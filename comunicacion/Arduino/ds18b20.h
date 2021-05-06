#include <OneWire.h>                 //Se importan las librerías
#include <DallasTemperature.h>

float ds1820(int Pin) {

  OneWire ourWire(Pin);
  DallasTemperature sensors(&ourWire);
  
  sensors.begin();  
  sensors.requestTemperatures();           //Prepara el sensor para la lectura
  
                                           //Se inician los sensores
  float temp = sensors.getTempCByIndex(0); //Se lee e imprime la temperatura en grados Centigrados
  delay(50);
return (temp);  
}
