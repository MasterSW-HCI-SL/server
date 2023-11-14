import os
from flask import Flask, jsonify, request
import json

x =  '{ "message":"fsa"}'

def get_front():
    return x