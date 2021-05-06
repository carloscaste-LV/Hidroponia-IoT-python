import json
import time
from random import random
from flask import Flask, render_template
import requests
import pyrebase

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

 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/distancia')
def Distancia():
    data = db.child("distancia").get().val()
    data = list(filter(None, data))
    data = list(map(float, data))
    
    labels = db.child("hora").get().val()
    labels = list(filter(None, labels)) 
    #/////////////////////////////////////////////

    x_labels = []
    i = 0
    for i in range(len(labels)):
        x_labels.append("'{}'".format(labels[i]))
    x_labels = ','.join(x_labels)
    x_labels = "{}".format(x_labels)
    
    sd = x_labels
    
    return render_template('distancia.html',sd=sd,data=data)

@app.route('/tds')
def Tds():
    data = db.child("tds").get().val()
    data = list(filter(None, data))
    data = list(map(float, data))
    
    labels = db.child("hora").get().val()
    labels = list(filter(None, labels)) 
    #/////////////////////////////////////////////

    x_labels = []
    i = 0
    for i in range(len(labels)):
        x_labels.append("'{}'".format(labels[i]))
    x_labels = ','.join(x_labels)
    x_labels = "{}".format(x_labels)
    
    sd = x_labels
    
    return render_template('tds.html',sd=sd,data=data)

@app.route('/ph')
def pH():
    data = db.child("ph").get().val()
    data = list(filter(None, data))
    data = list(map(float, data))
    
    labels = db.child("hora").get().val()
    labels = list(filter(None, labels)) 
    #/////////////////////////////////////////////

    x_labels = []
    i = 0
    for i in range(len(labels)):
        x_labels.append("'{}'".format(labels[i]))
    x_labels = ','.join(x_labels)
    x_labels = "{}".format(x_labels)
    
    sd = x_labels
    
    return render_template('pH.html',sd=sd,data=data)

@app.route('/temperatura_agua')
def Temperatura_agua():
    data = db.child("temperatura").get().val()
    data = list(filter(None, data))
    data = list(map(float, data))
    
    labels = db.child("hora").get().val()
    labels = list(filter(None, labels)) 
    #/////////////////////////////////////////////

    x_labels = []
    i = 0
    for i in range(len(labels)):
        x_labels.append("'{}'".format(labels[i]))
    x_labels = ','.join(x_labels)
    x_labels = "{}".format(x_labels)
    
    sd = x_labels
    
    return render_template('temperatura_agua.html',sd=sd,data=data)

#////////////Imagenes///////////////////
@app.route('/slides')
def slides():
    return render_template("slides.html")



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5010)