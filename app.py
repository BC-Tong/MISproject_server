from typing import Text
import flask
from flask import Flask
from flask import request

from flask import flash
from flask import redirect
from flask import url_for
from flask import session

import sqlite3
import os


app = flask.Flask(__name__)

def register_action():
    userAccount  = int(request.form['Account'])
    userPassword = int(request.form['Password'])
    
    con = sqlite3.connect('db_MISproject.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user(userAccount,userPassword) values(?,?)",(userAccount,userPassword))
    com.commit()
    con.close()
    return '註冊成功'

@app.route('/', methods=['GET','POST'])
def handle_call():
    return "Successfully Connected!!!"

@app.route('/register', methods=['GET','POST'])
def register_getData():
    if request.method=='POST':
        return register_action()
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

    
'''
@app.route('/save', methods=['POST'])
def handle_save():
    account=str(request.form['num1'])
    password=str(request.form['num2'])
    return (account,password)
'''



