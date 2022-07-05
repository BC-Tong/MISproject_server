from flask import Flask, request
import sqlite3, os, sys

os.path.join(__file__, 'mywebsite.db')
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname('mywebsite.db')))


app = Flask(__name__)


def register_action():
    
    
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    sex = request.form['sex']
    birthdate = request.form['birthdate']

    if not username:
        return '請輸入username'
    elif not email:
        return '請輸入email'
    elif not password:
        return '請輸入password'
    elif not sex:
        return '請輸入password'
    elif not birthdate:
        return '請輸入出生年月日'
    

    con =sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    
    cur.execute(f'SELECT * FROM user WHERE `email` = "{email}"')
    queryresult = cur.fetchone
    if queryresult:
        return 'email重複,請使用另一個email'
        
    cur.execute(f"INSERT INTO user (`username`, `email`, `password`, `sex`, `birthdate`) VALUES ('{username}','{email}','{password}', '{sex}', '{birthdate}')")
    con.commit()
    con.close()
    return '註冊成功'

def login_check(email, password):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT * FROM user WHERE `email`='"+email+"'AND `password`='"+password+"'")
    results = cur.fetchall()
    con.close()

    if results:
        return True
    else:
        return False


def login_action(email):
    con = sqlite3.connect('mywebsite.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT username FROM user WHERE `email`='"+email+"'")
    con.close
    result = querydata.fetchone()
    if result:
        return "你好" + str(result[0])
    else:
        return "此會員沒有資料"


@app.route('/')
def hello_world():
    print(__name__)
    return 'hello!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        if(login_check(email, password)):
            return login_action(email)
        else:
            return '查無此會員'
            
    else:
        login_check('jack90325@gmail.com', 'jack')
        return login_action('jack90325@gmail.com')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return register_action()
    else:
        return 'wrong method'

@app.route('/test', methods=['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        email = request.form['username']
        password = request.form['password']
        return (email)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)


'''
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

def login_check(userName,userPassword):
    con = sqlite3.connect('db_MISproject.db')
    cur = con.cursor()
    querydata = cur.execute("SELECT * FROM user WHERE userAccount=? AND userPassword=?",(userName,userPassword))
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
        a="123"
        
        return register_action()
        #return jsonify(userName=userName ,userPassword=userPassword ,userMail=userMail,userGender=userGender,userBirthday=userBirthday)
        #return a
    
    
@app.route('/login', methods=['GET','POST'])
def login():
    userName  = int(request.form['Name'])
    userPassword = int(request.form['Password'])
    
    if request.method=='POST':
        result = login_check(userName,userPassword)
        if result:
            return "1"        #1表示登入成功
        else:
            return "0"        #0表示登入失敗
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
'''



