import os
from flask import Flask, jsonify, request
import json

x =  '{ "message":"front_class"}'

def get_front():
    return x