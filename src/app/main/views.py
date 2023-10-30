from flask import Blueprint

main=Blueprint('main',__name__)

@main.route('/welcome',methods=['GET'])
def welcome():
    return "welcome"

@main.route('/login')
def login():
    return "login"