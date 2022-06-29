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

#conn = sqlite3.connect('db_MISproject.db')
#conn.execute('CREATE TABLE User (userAccount integer primary key, userPassword integer)')
#conn.close()

@app.route('/', methods=['GET','POST'])
def handle_call():
    return "Successfully Connected!!!"

@app.route('/register', methods=['GET','POST'])
def register_getData():
    #int 只是用來測試用
    userAccount  = int(request.form['Account'])
    userPassword = int(request.form['Password'])
    summary = userAccount+userPassword
    '''
    if request.method=='POST':
        try:
            con=sqlite3.connect('db_MISproject.db')
            cur=con.cursor()
            cur.execute("insert into User(userAccount,userPassword) values(?,?)",(userAccount,userPassword))
            con.comit()
            msg = "Record successfully added"
            
        except:
            return("Error in insert Operation","danger")
        finally:
            #return "value1"+userAccount+"value2"+userPassword
            con.close()
    '''
    return str(summary)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


'''
@app.route('/save', methods=['POST'])
def handle_save():
    account=str(request.form['num1'])
    password=str(request.form['num2'])
    return (account,password)
'''



