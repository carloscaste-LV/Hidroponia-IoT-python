import time

from mediciones import Medicion,db
import threading
medicion = Medicion()

hora = []
distancia = []
tds = []
ph = []
temperatura_agua = []

def nuevo_valor():
        while(1):
            time.sleep(5)
            i = db.child("i").get().val()
            i = int(i)+1
            while(1):
                j = int(db.child("i").get().val())
                
                if j >= i:            
                    break
            
            hora.append(medicion.hora())
            db.child("hora").set(hora)
            
            distancia.append(medicion.distancia())
            db.child("distancia").set(distancia)            
            
            ph.append(medicion.ph())
            db.child("ph").set(ph)
            
            temperatura_agua.append(medicion.temperatura_agua())
            if temperatura_agua == str:
                temperatura_agua[(len(temperatura_agua))-1] = temperatura_agua[(len(temperatura_agua))-2] 
            db.child("temperatura").set(temperatura_agua)
           
            tds.append(medicion.tds())
            db.child("tds").set(tds)
            
thread_y = threading.Thread(target=nuevo_valor)
thread_y.start()

while(1):             
    data = db.child("distancia").get().val()
    data = list(filter(None, data))
    
    
    labels = db.child("hora").get().val()
    labels = list(filter(None, labels)) 
    #/////////////////////////////////////////////

    x_labels = []
    i = 0
    for i in range(len(labels)):
        x_labels.append("'{}'".format(labels[i]))
    x_labels = ','.join(x_labels)
    x_labels = "{}".format(x_labels)
    time.sleep(5)
    print(x_labels)