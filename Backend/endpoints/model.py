import os
from flask import Flask, jsonify, request
import json

x =  '{ "message":"model_class"}'

def get_front():
    return x