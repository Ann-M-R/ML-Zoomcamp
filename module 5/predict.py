# %%
from flask import Flask
from flask import request  #to process json requests
from flask import jsonify

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# %%
import pickle

# %%
model_file = 'model_C=1.0.bin'
model_file

# %%
with open(model_file, 'rb') as f_in:
    dv,model = pickle.load(f_in)


app = Flask('churn')  

@app.route('/predict',methods = ['POST'])  #which address and which method
def predict():
    customer = request.get_json()   #turms it into a python dictionary
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]  #first row second column
    churn = y_pred>=0.5 #making the decison here, basically is true is pred greater than 0.5

    result = {
        'churn_probability': float(y_pred), #here also turning into normal float 
        'churn': bool(churn)  #turn numpy bool into usual py boolean otherwise error will come wen requested
    }
    
    return jsonify(result)


if __name__ == "__main__":   #top-level code” is called an entry point to the application.``
    app.run(debug = True, host = '0.0.0.0', port = 9696)  #debug mode, 0.0.0.0 is local host and a port


#we get error if we simply run the app in browser and query localhost cos get method is not there so we try from a jupyter notebook 05-predict-test