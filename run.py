from flask import Flask,make_response
from http import HTTPStatus
from src.app import create_app

app=create_app('default')

app=Flask(__name__)

@app.route('/welcome',methods=['GET'])
def welcome():
    return "ciao da wio2023",HTTPStatus.CREATED

@app.route('/login')
def login():
    return "login"