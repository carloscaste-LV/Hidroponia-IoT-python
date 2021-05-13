# Red Neuronal Recurrente

# Part 1 - Pre Procesamiento de Datos
for i in range(1):
    # Importando Librerias
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    
    # Importando Set de Entrenamiento
    dataset_train = pd.read_csv('dataset6_train.csv')
    training_set = dataset_train.iloc[:, 3:5].values
    
    # Escalado de Categorias
    from sklearn.preprocessing import MinMaxScaler
    sc = MinMaxScaler(feature_range = (0, 1))
    training_set_scaled = sc.fit_transform(training_set)
    
    def ColumnaTrain(n):
        # Creando Estructura de Datos con 168 Pasos y 168 outputs
        X_train = []    
        for i in range(168, 743):
            X_train.append(training_set_scaled[i-168:i, n])
            
        X_train= np.array(X_train)
        
        # Remodelacion
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        return X_train
    
    y_train = []
    i = 0
    for i in range(186, 761):    
        
        y_train.append(training_set_scaled[i-168:i, 0])
    
    y_train = np.array(y_train)
    y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[1]))
    X_train = np.concatenate([ColumnaTrain(0),ColumnaTrain(1)],axis=2)
    
    # Part 2 - Armando la Red Neuronal Recurrente
    
    # Importando Librerias
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import LSTM
    from keras.layers import Dropout
    from keras.layers import Reshape
    
    # Iniciando RNR
    regressor = Sequential()
    
    # Primera capa LSTM y Regularizacion de Dropout
    regressor.add(LSTM(units = 100, return_sequences = True, input_shape = (X_train.shape[1],X_train.shape[2])))
    regressor.add(Dropout(0.2))
    
    # Segunda capa LSTM y Regularizacion de Dropout
    regressor.add(LSTM(units = 100, return_sequences = True))
    regressor.add(Dropout(0.2))
    
    # Tercera capa LSTM y Regularizacion de Dropout
    regressor.add(LSTM(units = 100, return_sequences = True))
    regressor.add(Dropout(0.2))

    regressor.add(LSTM(units = 100, return_sequences = True))
    regressor.add(Dropout(0.2))


 
    # Cuarta capa LSTM y Regularizacion de Dropout
    regressor.add(LSTM(units = 100))
    regressor.add(Dropout(0.2))
    
    # Capa Output / Salida
    regressor.add(Dense(units = 168))
    regressor.add(Reshape((168,1)))
    
    # Compilando RNR
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    
    # Encajando Red Neuronal En Set de Entrenamiento
    regressor.fit(X_train, y_train, epochs = 200, batch_size = 32)
    
    
    
    # Part 3 - Haciendo Predicciones y Visualizando Datos
    
    # Obteniendo los valores para probar rnr
    dataset_test = pd.read_csv('dataset6_test.csv')
    real_ph_price = dataset_test.iloc[:, 4:5].values
    
    training_set = dataset_train.iloc[:, 4:5].values
    
    sc = MinMaxScaler(feature_range = (0, 1))
    training_set_scaled = sc.fit_transform(training_set)
    
    # Obteniendo el ph Predicho
    def ColumnaTest(col):
        dataset_total = pd.concat((dataset_train[col], dataset_test[col]), axis = 0)
        inputs = dataset_total[len(dataset_total) - len(dataset_test) - 168:].values
        inputs = inputs.reshape(-1,1)
        inputs = sc.transform(inputs)
        X_test = []
        i = 0
        for i in range(168, 256):
            X_test.append(inputs[i-168:i, 0])
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        
        return X_test
    
    #Contruir matriz 
    X_test = np.concatenate([ColumnaTest("Sensor__Sensor1__ph"),
                            ColumnaTest("Sensor__Sensor1__ph")],axis=2)
    
    
    
    predicted_ph = regressor.predict(X_test)
    predicted_ph= predicted_ph.reshape((predicted_ph.shape[0], -1))
    
    
    predicted_ph = sc.inverse_transform(predicted_ph)
    
    prediccion = []
    for i in range(88):
        prediccion.append(predicted_ph[i,0])
    for i in range(168):
        prediccion.append(predicted_ph[88,i])
    # Visualizando Resultados
    plt.plot(real_ph_price, color = 'black', label = 'Real pH',linewidth=1)
    plt.plot(prediccion, color = 'black', label = 'Predicted pH', linestyle="-.",  linewidth=1)
    plt.title('')
    plt.xlabel('Time')
    plt.ylabel('pH')
    plt.legend()
    plt.show()
