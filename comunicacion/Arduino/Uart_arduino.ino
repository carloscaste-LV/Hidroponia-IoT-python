#include <SoftwareSerial.h>
#include "ds18b20.h"
#include "hcsr04.h"
#include "GravityTDS.h"
#include "returnTds.h" 
#include "ph.h" 

char resulttds[20]; 
char resultdis[20];
char resulttemp[20];
char resultph[20];

int rele=8;




SoftwareSerial mySerial(0, 1); // RX, TX
void setup()
{
  // Open serial communications and wait for port to open:
  mySerial.begin(115200);
  pinMode(8, OUTPUT);
  delay(1000*5);
  
}



void loop() // run ovehr and over
{
/*mySerial write solo admite datos char, entonces a los datos tipo int
  los convertimos en str y los srt a char*/
  
 String TDS = String(tds()); //Sensor de ppm's Pin A1
 TDS.toCharArray(resulttds, 20);

 String PH = String(ph()); //Sensor de ph Pin A0
 PH.toCharArray(resultph, 20);

 String DISTANCIA = String(distancia_cm (3,4));//Sensor de distancia triger(Pin3)/ecco(Pin4) 
 DISTANCIA.toCharArray(resultdis, 20);//

 String TEMPERATURA = String(ds1820(2));// Sensor de temperatura pin Pin 2
 TEMPERATURA.toCharArray(resulttemp, 20);


//Condicionales de transmision de datos Uart//
    
    
    if (mySerial.available()>0){
    byte lectura = '9';
   lectura = mySerial.read();

    delay(5);
    
    
    if(lectura == '1'){
      mySerial.write(resulttds);
 

    } 
    if(lectura == '2'){
      mySerial.write(resultdis);
 

    }  
    if(lectura == '3'){
      mySerial.write(resulttemp);
      

    }  
    if(lectura == '4'){
      mySerial.write(resultph);

    }
    //Apagar y encender Bomba
        
        if(lectura == '5'){
          digitalWrite(rele, HIGH); 
          mySerial.write('1');
        }  
        if(lectura == '6'){
          digitalWrite(rele, LOW);
          mySerial.write('1');  
    //////////////////////////


      
     
    
   }       
 }
}

 







 
