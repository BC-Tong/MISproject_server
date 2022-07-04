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
    
    userAccount  = request.form['Account']
    userPassword = request.form['Password']
    '''
    con = sqlite3.connect('db_MISproject.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user(userAccount,userPassword) values(?,?)",(userAccount,userPassword))
    com.commit()
    con.close()
    '''
    return '註冊成功'

def login_check(userAccount,userPassword):
    con = sqlite3.connect('db_MISproject.db')
    cur = con.cursor()
    querydata = cur.execute("SELECT * FROM user WHERE userAccount=? AND userPassword=?",(userAccount,userPassword))
    results = cur.fetchall()
    con.close
    if results:
        return True
    else:
        return False

@app.route('/', methods=['GET','POST'])
def handle_call():
    return "Successfully Connected!!!"

@app.route('/register', methods=['GET','POST'])
def register_getData():
    if request.method=='POST':
        userAccount  = request.form['Account']
        userPassword = request.form['Password']
        return register_action()
    
@app.route('/login', methods=['GET','POST'])
def login():
    userAccount  = int(request.form['Account'])
    userPassword = int(request.form['Password'])
    if request.method=='POST':
        '''
        result = login_check(userAccount,userPassword)
        if result = True:
            return 1        #1表示登入成功
        else:
            return 0        #0表示登入失敗
        '''
        return 'flask login route'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



