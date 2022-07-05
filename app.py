from typing import Text
import flask
from flask import Flask
from flask import request

from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify

import sqlite3
import os


app = flask.Flask(__name__)

def register_action():
    #取得Data
    userName  = request.form['Name']
    userPassword = request.form['Password']
    userMail = request.form['Mail']
    userGender = request.form['Gender']
    userBirthday = request.form['Birthday']
    #連接db_MISproject.db
    con = sqlite3.connect('db_MISproject.db')
    cur = con.cursor()
    
    #檢查email
    cur.execute('SELECT * FROM User_table WHERE `UserMail` = "{userMail}"')
    queryresult = cur.fetchall()
    if queryresult:
        return 'email已存在，請使用另一個email'
    #檢查userName
    cur.execute('SELECT * FROM User_table WHERE `UserName` = "{userName}"')
    queryresult = cur.fetchall()
    if queryresult:
        return '該名稱已被使用，請使用另一個名稱'
    #將資料放入User_table中
    cur.execute("INSERT INTO User_table(UserName,UserPassword,UserMail,UserGender,UserBirthday) values(?,?)",(userName,userPassword,userMail,userGender,userBirthday))
    com.commit()
    con.close()
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
        a=123
        userName  = request.form['Name']
        userPassword = request.form['Password']
        userMail = request.form['Mail']
        userGender = request.form['Gender']
        userBirthday = request.form['Birthday']
        
        #return register_action()
        #return jsonify(userName=userName ,userPassword=userPassword ,userMail=userMail,userGender=userGender,userBirthday=userBirthday)
        return a
    
    
@app.route('/login', methods=['GET','POST'])
def login():
    userAccount  = int(request.form['Account'])
    userPassword = int(request.form['Password'])
    '''
    if request.method=='POST':
        result = login_check(userAccount,userPassword)
        if result = True:
            return 1        #1表示登入成功
        else:
            return 0        #0表示登入失敗
    '''
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



