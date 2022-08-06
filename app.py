# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, json, session
from datetime import timedelta
import sqlite3, os, sys
import collections

os.path.join(__file__, 'MISProject_database.db')
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname('MISProject_database.db')))

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(__name__)
    return 'hello!'        
        
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
    
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    
    emailcheck = cur.execute(f"SELECT * FROM User_table WHERE `UserMail`='"+email+"'")
    queryresult = emailcheck.fetchone()
    if queryresult:
        return 'email重複,請使用另一個email'
    
    cur.execute(f"INSERT INTO User_table (`UserName`, `UserMail`, `UserPassword`, `UserSex`, `UserBirthdate`,`AccountCreateTime`) VALUES ('{username}','{email}','{password}', '{sex}', '{birthdate}', datetime('now'))")
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
    querydata = cur.execute(f"SELECT * FROM User_table WHERE `UserMail`='"+email+"'")
    con.close
    result = querydata.fetchone()
    if result:
        #回傳當前登入者的基本資料
        return '{} {} {} {} {} {} {}'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
    else:
        return "此會員沒有資料"

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

@app.route('/getExp',methods=['GET','POST'])
def getExp():
    if request.method == 'POST':
        username = request.form['username']
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT exp FROM exp_table WHERE `username`='{username}'")
    result = querydata.fetchone()
    con.close
    if result:
        return '{}'.format(result[0])
    else:
        return "LV.0"

def print_AllMenuName():
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT MenuName FROM Menu_table")
    con.close
    result = querydata.fetchall()
    return result        
  
@app.route('/printAllMenu', methods=['GET', 'POST'])
def print():
    result = print_AllMenuName()
    if result:
        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],result[14])
    else:
        return "error-menuName not found in db"

@app.route('printmostdomenu',methods=['GET','POST'])
def printmostdomenu():
    if request.method == 'POST':
        userid = int(request.form['userid'])
    menu1 = "促進血液循環"
    menu2 = "全身放鬆"
    menu3 = "核心訓練"
    retrun '{} {}'.format(userid,menu1)
    '''
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata1 = cur.execute(f"SELECT record_id FROM Record_table WHERE `user_id`='{userid}' AND `menuname`='{menu1}' ")
    result1 = querydata1.fetchall()
    con.close
    
    if result1:
        objects_list = []
        for row in result1:
            d = collections.OrderedDict()
            d["record_id"] = row[0]
            objects_list.append(d)
        return objects_list
        #return '{} {} {}'.format("促進血液循環共做",result1[0],"次")
    else:
        return "count menu failed OR do not have record"
    '''
def insert_record_table(userid,menuname,menucal,score):
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO Record_table (`user_id`, `menuname`,`menucal`, `score`, `finish_time`) VALUES( '{userid}','{menuname}','{menucal}','{score}', date('now'))")
    con.commit()
    con.close()
    return "Success"

def check_exp_data(userid):
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT * FROM exp_table WHERE `user_id`='{userid}' ")
    result = querydata.fetchone()
    con.close()
    if result:
        return "Have Data"
    else:
        return "No Data"

def get_new_exp(userid,score):
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT exp FROM exp_table WHERE `user_id`='{userid}'")
    result = querydata.fetchone()
    con.close()
    exp = result[0]
    new_exp = exp + score
    return int(new_exp)

def insert_exp_table(userid,username,score):
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO exp_table (`user_id`, `username`,`exp`) VALUES( '{userid}','{username}','{score}' )")
    con.commit()
    con.close()
    return "Success insert"

def update_exp_table(userid,new_exp):
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"UPDATE exp_table SET `exp`='{new_exp}' WHERE `user_id`='{userid}' ")
    con.commit()
    con.close()
    return "Success update"
    
@app.route('/record', methods=['GET', 'POST'])
def record():
    if request.method == 'POST':
        userid = int(request.form['userid'])
        username = request.form['username']
        score = int(request.form['score'])
        menuname = request.form['menuname']
        menucal = request.form['menucal']
    result1 = insert_record_table(userid,menuname,menucal,score)
    
    checkstr = check_exp_data(userid)
    if result1 == "Success":
        if checkstr == "Have Data":
            new_exp = get_new_exp(userid,score)
            updateResult = update_exp_table(userid,new_exp)
            if updateResult == "Success update":
                return '{} {}'.format("Successful insert record & update new_exp ->",new_exp)
            else:
                return "update failed"
        elif checkstr == "No Data":
            insertResult = insert_exp_table(userid,username,score)
            if insertResult == "Success insert":
                return '{} {}'.format("Successful insert record & exp ->",score)
            else:
                return "insert exp failed"
    else:
        return "insert record failed"
    
@app.route('/printrecord', methods=['GET', 'POST'])
def printrecord():
    if request.method == 'POST':
        userid = int(request.form['userid'])
        
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT * FROM Record_table WHERE user_id ='{userid}' ORDER BY record_id DESC LIMIT 10 ")
    result = querydata.fetchall()
    con.close()
    if result:
        #return json.dumps(result, ensure_ascii=False).encode('utf8')
        objects_list = []
        for row in result:
            d = collections.OrderedDict()
            d["finish_time"] = row[5]
            d["menuname"] = row[2]
            d["calories"] = row[3]
            d["score"] = row[4]
            objects_list.append(d)
        return json.dumps(objects_list,indent=2, ensure_ascii=False).encode('utf8')
    else:
        return "DB do not have data"    
    
@app.route('/scoreupload', methods=['GET', 'POST'])
def score_upload():
    if request.method == 'POST':
        score = request.form['score']
        return str(score)
    
@app.route('/test', methods=['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        email = request.form['username']
        password = request.form['password']
        return (email)

def insert_rank(new_user_name,new_score):
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO Rank_table (`username`, `userrank`) VALUES ('{new_user_name}','{new_score}')")
    con.commit()
    con.close
    return "Success"
     
@app.route('/storeRank', methods=['GET', 'POST'])
def storeRank():
    if request.method == 'POST':
        data = request.get_json()
        new_user_name = data['userName']
        new_score = data['score']
        
        result = insert_rank(new_user_name,new_score)
        if result == "Success":
            con = sqlite3.connect('MISProject_database.db')
            cur = con.cursor()
            querydata = cur.execute(f"SELECT username,userrank FROM Rank_table WHERE rank_id = (SELECT MAX(rank_id) FROM Rank_table)")
            result1 = querydata.fetchone()
            con.close()
            return '{} {} {} {}'.format("insert success with username:",result1[0]," rank:",result1[1])
        else:
            return "insert failed"

@app.route('/getTop20Rank', methods=['GET', 'POST'])
def getTop20Rankt():
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT username,userrank FROM Rank_table ORDER BY userrank DESC LIMIT 20")
    result = querydata.fetchall()
    con.close()
    if result:
        return json.dumps(result, ensure_ascii=False).encode('utf8')
    else:
        return "failed get data from DB"    

def get_exp(username):
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT exp FROM exp_table WHERE `username`='{username}'")
    result = querydata.fetchone()
    con.close
    if result:
        return result
    else:
        return False
    
def get_sex(username):
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT UserSex FROM User_table WHERE `UserName`='{username}'")
    result = querydata.fetchone()
    con.close
    if result:
        return result
    else:
        return False    

#傳exp到unity
@app.route('/getuserdata', methods=['GET', 'POST'])
def getuserdata():
    if request.method == 'POST':
        data = request.get_json()
        username = data['userName']
    result = get_exp(username)
    result2 = get_sex(username)
    if result:
        if result2:
            return '{} {} {} {}'.format("Exp: ",result[0]," Gender: ",result2[0])
        else:
            return '{} {} {}'.format("Exp: ",result[0]," But do not get gender from DB")
    else:
        return "get_exp fail or DB do not have data"
        
if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
    app.run(host='127.0.0.1', port=5050, debug=True)






