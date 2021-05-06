#include <HCSR04.h>


float distancia_cm (int triggerPin,int echoPin){
UltraSonicDistanceSensor distanceSensor(triggerPin, echoPin);
double distance = distanceSensor.measureDistanceCm();
delay(500);
return distance;
}
