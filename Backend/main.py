import os
from flask import Flask, request, jsonify, make_response
import endpoints.front as front
import endpoints.fsa as fsa
import endpoints.model as model
import json

app = Flask(__name__)


#--------------- GET ---------------

#GET main page
@app.route("/", methods=["GET"])
def get_main():
    try:
        res = front.get_front()

        return res
    except:
        return "exception"
    

#GET FSA
@app.route("/fsa", methods=["GET"])
def get_fsa():
    try:
        res = fsa.get_fsa()

        return res
    except:
        return "exception"

#GET MI model
@app.route("/model", methods=["GET"])
def get_model():
    try:
        res = model.get_model()
        
        return res
    except:
        return "exception"

#--------------- POST ---------------

#@app.route("/endpoint", methods=["POST"])
#def post_model():
#    return "post_model", 201

if __name__ == '__main__':
    app.run()