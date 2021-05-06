# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:46:12 2021

@author: CarlosCaste
"""

import pyrebase
import threading
import time
firebaseConfing= {    

    "apiKey": "AIzaSyD3LHB9TgW4pUa0v9yxwjFXPyQ19ywrcak",
    "authDomain": "control-inteligente-310605.firebaseapp.com",
    "databaseURL": "https://control-inteligente-310605-default-rtdb.firebaseio.com/",
    "projectId": "control-inteligente-310605",
    "storageBucket": "control-inteligente-310605.appspot.com",
    "messagingSenderId": "344504730863",
    "appId": "1:344504730863:web:ba50f7b709cf394cf6c71a",
    "measurementId": "G-BT0ZNPRYQL"
}
firebase  = pyrebase.pyrebase.initialize_app(firebaseConfing)
db = firebase.database()




def Temperatura():
    i = db.child("i").get().val()
    i = int(i)-1
    temperatura = db.child("Sensor").child("Sensor1").child(str(i)).child("temperatura").get().val()
    return (temperatura)
def Tds():
    i = db.child("i").get().val()
    i = int(i)-1
    Tds = db.child("Sensor").child("Sensor1").child(str(i)).child("tds").get().val()
    return (Tds)
def Distancia():
    i = db.child("i").get().val()
    i = int(i)-1
    distancia = db.child("Sensor").child("Sensor1").child(str(i)).child("distancia").get().val() 
    return (distancia)
def Tiempo():
    i = db.child("i").get().val()
    i = int(i)-1
    distancia = db.child("Sensor").child("Sensor1").child(str(i)).child("Hora").get().val() 
    return (distancia)
def pH():
    i = db.child("i").get().val()
    i = int(i)-1
    distancia = db.child("Sensor").child("Sensor1").child(str(i)).child("ph").get().val() 
    return (distancia)



class Medicion:
    def __init__(self):
        pass 
    def tds(self):
        return (Tds())
    def distancia(self):
        return (Distancia())
    def temperatura_agua(self): 
        return (Temperatura())
    def hora(self): 
        return (Tiempo())
    def ph(self):
        return (pH())

