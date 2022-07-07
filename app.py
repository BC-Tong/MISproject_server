from flask import Flask, request
import sqlite3, os, sys
import re

os.path.join(__file__, 'MISProject_database.db')
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname('MISProject_database.db')))


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
    #elif email.find("@") == -1 or not email.endswith('.com'):
    #    return 'email格式錯誤'
    elif not password:
        return '請輸入password'
    elif len(password)<4:
        return '密碼必須大於4碼' 
    elif not sex:
        return '請輸入性別'
    elif not birthdate:
        return '請輸入出生年月日'
    #elif birthday
    

    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    
    #不管輸入啥都 return 'email重複,請使用另一個email' 明天看
    #cur.execute(f'SELECT * FROM User_table WHERE `UserMail` = "{email}"')
    #queryresult = cur.fetchone
    #if queryresult:
    #    return 'email重複,請使用另一個email'
    
    #資料好像沒進資料庫 明天看
    cur.execute(f"INSERT INTO User_table (`UserName`, `UserMail`, `UserPassword`, `UserSex`, `UserBirthdate`) VALUES ('{username}','{email}','{password}', '{sex}', '{birthdate}')")
    con.commit()
    con.close()
    return '註冊成功'

def login_check(email, password):
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT * FROM User_table WHERE `UserMail`='"+email+"'AND `UserPassword`='"+password+"'")
    results = cur.fetchall()
    con.close()

    if results:
        return True
    else:
        return False


def login_action(email):
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT UserName FROM User_table WHERE `UserMail`='"+email+"'")
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






