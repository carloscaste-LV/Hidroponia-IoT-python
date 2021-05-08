# Hidroponia-IoT
 _-Python-Flask-Firebase-Arduino-Micropython_

## Hardware del proyecto

- Arduino UNO
- ESP8266
- PH-4502C
- Sonda de sensor ph: Sonda PH BNC
- Sensor tds: Gravity: Analog TDS Sensor
- Sensor de distancia: hc-sr04
- Sensor de temperatura: ds18b20
- Actuadores: bomba sumergible
- Relevador

# _MycroPython_
>MicroPython es una implementación sencilla y eficiente del lenguaje de programación Python 3 que incluye un pequeño subconjunto de la biblioteca estándar de Python y está optimizado para ejecutarse en microcontroladores y en entornos restringidos.

La idea de utilizar el framework MycroPython es manajar la mayor parte del proyecto en un solo lenguaje de programacion, para utilizae MycroPython nesesitamos 2 cosas:

-   Un IDE para programar.
-   El framework que instalaremos en nuestro ESP8266.

El IDE utilizado fue [uPyCraft]( https://randomnerdtutorials.com/uPyCraftWindows) y el framework fue descargado desde la pagina oficial de [MycroPython](https://micropython.org/resources/firmware/esp8266-20210420-unstable-v1.15.bin). Para comunicar ESP8266 con firebase utilizamos los modulos  publicados por [vishal-android-freak](https://github.com/vishal-android-freak/firebase-micropython-esp32) los cuales fuero programados para utilizarse en la tarjeta ESP32 por lo que tiene algunos metodos que nustra tarjeta no soporta y de intentar usarlos nuestro codigo no funcionara, en particular el metodo que debemos eliminar para que el modulo de vishal-android-freak funcione en nuestro dispositivo es __thread__.
