# Util contains all the core routines 

# Create global variables for model and data columns 
import json
import pickle
import numpy as np


# __data_columns = None
__model = None

# STEP: prediction of stability number
def get_stability_number(D, GSI, mi, beta, kh): 
    x = np.zeros(5)
    x[0] =  D
    x[1] =  GSI
    x[2] = mi 
    x[3] = beta
    x[4] = kh

    x = np.reshape(x,(1,5)) # creata a (1X5) array

    stability_number =  (__model.predict(x)[0]) # where x is a 2D array return the predicted stability number to 3 decimal places
    stability_number = round(stability_number.tolist(), 3) # datatype of the XGBoost model output is a numpy float32, convert it to a list to make it a default Python type
    return stability_number

# STEP:  variables and model

def load_saved_artifacts():
    print ("loading saved artifacts...start")
    # global __data_columns
    global __model

    # with open("./Server/artifacts/columns.json", 'r') as f:
        # __data_columns = json.load(f)['data_columns'] #data_columns key

    with open("./Server/artifacts/GA-XGBoost-stability-predictor-model.pickle", 'rb') as f: # load model
        __model = pickle.load(f)
        print ('loading saved artifacts done...')

#def get_column_names():
    #return __data_columns
    
if __name__ == '__main__':
    load_saved_artifacts()
    # print (get_column_names()) 
    print(get_stability_number(0.9, 50, 35, 75, 0.4))