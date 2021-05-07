

#==========================================Librerias=======================================#

import time
from machine import RTC



# synchronize RTC with ntp
import ntptime


import startup
import ufirebase as firebase

from comunicacion import Uaart  




#=====================================Conexion internet=====================================#
startup.wlan_connect("MEGACABLE-UZ7BSY", "93214985")
#startup.wlan_connect("INFINITUM4119", "hWzA1D2tm7")


URL = "https://control-inteligente-310605-default-rtdb.firebaseio.com/"
#=======================================Tiempo Fecha=========================================#
rtc = RTC()


#fecha(0:year, 1:month, 2:day, 4:hour, 5:minute, 6:second)
def hora():
  ntptime.settime() 
  date = rtc.datetime()
  if ((int(date[4]) - 7) <= 0):
      return (str(int(date[4])+17) + ":" +str(date[5]))
  else:
      return (str(int(date[4])-7) + ":" +str(date[5]))

def fecha():
  ntptime.settime() 
  date = rtc.datetime()  
  return (str(date[0])+":"+str(date[1])+":"+str(date[2]))



#=========================================Sensores=============================================#
def TDS():  
  return Uaart(b'1').decode('utf-8')


def DISTANCIA(): 
  return Uaart(b'2').decode('utf-8')


def TEMPERATURA(): 
  return Uaart(b'3').decode('utf-8')

def PH(): 
  return Uaart(b'4').decode('utf-8')

#=========================================Actuadores=============================================# 
def Bomba():
    estado=firebase.get(URL+"bomba")  
    estado=(int(estado)).decode()
    return Uaart(estado).decode('utf-8')

#================================Transmicion de datos tiempo real===============================#

  
i=firebase.get(URL+"i")
def  mensaje():
    global i
    i=int(i)+1
    firebase.patch(URL, {'i':str(i)})
    


    firebase.patch(URL, {'Sensor/Sensor1/'+str(i)+"/Fecha": fecha(),
                         'Sensor/Sensor1/'+str(i)+"/Hora": hora(),
                         'Sensor/Sensor1/'+str(i)+"/tds": TDS(),
                         'Sensor/Sensor1/'+str(i)+"/distancia": DISTANCIA(),
                         'Sensor/Sensor1/'+str(i)+"/ph": PH(),
                         'Sensor/Sensor1/'+str(i)+"/temperatura": TEMPERATURA()})



    
    
    time.sleep(56)
   
  

while(1):
    try:
      mensaje()
      Bomba()
      time.sleep(1)
    except:
      Uaart(b'5').decode('utf-8') #Apagar bomba
      startup.wlan_connect("MEGACABLE-UZ7BSY", "93214985")
 


#=================================================================================================#



