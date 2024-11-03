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
model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)  # Load DictVectorizer

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)  # Load LogisticRegression model

app = Flask('app')  
# %%
@app.route('/predict',methods = ['POST'])  
def predict():
    client = request.get_json()   
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]  

    result = {
        'probability': float(y_pred)
    }
    
    return jsonify(result)

if __name__ == "__main__":   
    app.run(debug = True, host = '0.0.0.0', port = 9696)