from flask import Flask

app = Flask('ping')   #creating a flask app

#add decorator i.e. add some extra functionality to the app
#in this case this functionality allows us to make this a web service

@app.route('/ping',methods = ['GET'])  #which address and which method
def ping():
    return "pong"

if __name__ == "__main__":   #top-level code” is called an entry point to the application.``
    app.run(debug = True, host = '0.0.0.0', port = 9696)  #debug mode, 0.0.0.0 is local host and a port