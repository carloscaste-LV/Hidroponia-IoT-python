# Hidroponía -IoT
 _-Python-Flask-Firebase-Arduino-Micropython_

## Hardware del proyecto

- Arduino UNO
- ESP8266
- PH-4502C
- Sonda de sensor pH: Sonda PH BNC
- Sensor tds: Gravity: Analog TDS Sensor
- Sensor de distancia: hc-sr04
- Sensor de temperatura: ds18b20
- Actuadores: bomba sumergible
- Relevador

# _MycroPython_
>“MicroPython es una implementación sencilla y eficiente del lenguaje de programación Python 3 que incluye un pequeño subconjunto de la biblioteca estándar de Python y está optimizado para ejecutarse en microcontroladores y en entornos restringidos”.

La idea de utilizar el framework MycroPython es manejar la mayor parte del proyecto en un solo lenguaje de programación, para utilizar MycroPython necesitamos 2 cosas:

-   Un IDE para programar.
-   El framework que instalaremos en nuestro ESP8266.

El IDE utilizado fue [uPyCraft]( https://randomnerdtutorials.com/uPyCraftWindows) y el framework fue descargado desde la pagina oficial de [MycroPython](https://micropython.org/download/esp8266/). Para comunicar ESP8266 con firebase utilizamos los módulos  publicados por [vishal-android-freak](https://github.com/vishal-android-freak/firebase-micropython-esp32) los cuales fueron programados para utilizarse en la tarjeta ESP32 por lo que tiene algunos métodos que nuestra tarjeta no soporta y de intentar usarlos nuestro Código no funcionara, en particular el método que debemos eliminar es __thread__.

# _Arduino_
>“Arduino es una compañía de desarrollo de software y hardware libres, así como una comunidad internacional que diseña y manufactura placas de desarrollo de hardware para construir dispositivos digitales y dispositivos interactivos que puedan detectar y controlar objetos del mundo real”.

La razón de usar Arduino es usar sus puertos analógicos y digitales para posteriormente enviar los datos recolectados al módulo wifi (el cual no cuenta con los suficientes puertos para cubrir las necesidades del proyecto).

Cabe destacar es recomendable hacer todo desde una sola placa que cuente con un módulo wifi y con los suficientes puertos analógicos para realizar el proyecto.

## Python
>Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional.

Python tiene 2 funciones principales en este proyecto crear una aplicación web y manejar la base de datos de firebase desde la misma, para ello es ideal usar 2 módulos; [pyrebase4](https://github.com/nhorvath/Pyrebase4) y [flask](https://flask.palletsprojects.com/en/1.1.x/).



## Hidroponía



