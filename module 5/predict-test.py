



# %%
import requests


# %%
url = 'http://localhost:9696/predict'

# %%
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}


# %%
requests.post(url, json = customer)

# %%
response = requests.post(url, json = customer).json()
if response['churn'] == True:
    print('sending promo email to customer')

# %%
#we get warning when running pythin script saying its a development server we need to use a wsgi server
#we use gunicorn pip install gunicorn
#we need to tell gunicorn where our app is - gunicorn run predict:app i.e the pyhton dile it needs to go to and the variable it is interested in
#but when we run from gunicorn the if statement with main is not considered so
#gunicorn --bind 0.0.0.0:9696 predict:app

#to run gunicorn on windows https://stackoverflow.com/questions/62788628/modulenotfounderror-no-module-named-fcntl install waitress

#waitress-serve --listen=*:8000 app:app



