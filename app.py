from flask import Flask, request, jsonify
import sqlite3, os, sys 

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
    #elif len(password)<5:
    #    return '密碼必須大於5碼' 
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
    

def print_AllMenuName():
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT MenuName FROM Menu_table")
    con.close
    result = querydata.fetchall()
    return result
        
@app.route('/printusername', methods=['GET', 'POST'])
def printname():
    userName = "1"
    return userName


@app.route('/printdomostmenu', methods=['GET', 'POST'])
def printmenu1():
    result = print_AllMenuName()
    if result:
        return '{} {} {}'.format(result[0],result[1],result[2])
    else:
        return "error-menuName not found in db"
    
@app.route('/printhotmenu', methods=['GET', 'POST'])
def printhot():
    result = print_AllMenuName()
    if result:
        return '{} {} {}'.format(result[1],result[2],result[3])
    else:
        return "error-menuName not found in db"
  
@app.route('/printAllMenu', methods=['GET', 'POST'])
def print():
    result = print_AllMenuName()
    if result:
        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],result[14])
    else:
        return "error-menuName not found in db"
'''下午版本    
@app.route('/record', methods=['GET', 'POST'])
def record():
    if(request.method == 'POST'):
        score = request.form['score']
        menuname = request.form['menuname']
        
        con =sqlite3.connect('MISProject_database.db')
        cur = con.cursor()
        cur.execute(f"INSERT INTO Record_table (`user_id`, `menuname`, `score`, `finish_time`) VALUES( 1,'{menuname}', '{score}', date('now'))")
        con.commit()
        con.close()
        return "successful insert"
        
@app.route('/printrecord', methods=['GET', 'POST'])
def printrecord():
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f'SELECT user_id,menuname,score,finish_time FROM Record_table WHERE record_id = (SELECT MAX(record_id)  FROM Record_table)')
    result = querydata.fetchone()
    con.close()
    
    menucarl = '100大卡' 
    
    if result:
        return '{} {} {} {}'.format(result[3],result[1],menucarl,result[2])
    else:
        return "error- not found data in db"    
'''
@app.route('/record', methods=['GET', 'POST'])
def record():
    if request.method == 'POST':
        userid = request.form['userid']
        score = request.form['score']
        menuname = request.form['menuname']
        menucal = request.form['menucal']  
        
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO Record_table (`user_id`, `menuname`,`menucal`, `score`, `finish_time`) VALUES( '{userid}','{menuname}','{menucal}','{score}', datetime('now'))")
    con.commit()
    con.close()
    return "successful insert"
        
@app.route('/printrecord', methods=['GET', 'POST'])
def printrecord():
    if request.method == 'POST':
        userid = request.form['userid']
        
    con =sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT user_id,menuname,menucal,score,finish_time FROM Record_table WHERE `user_id`='"+userid+"' AND record_id = (SELECT MAX(record_id)  FROM Record_table)")
    result = querydata.fetchone()
    con.close()
    
    if result:
        return '{} {} {} {}'.format(result[4],result[1],result[2],result[3])
    else:
        return "DB do not have data"
    
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
     
    
@app.route('/testunity', methods=['GET', 'POST'])
def testunity():
    if(request.method == 'POST'):
        data = request.get_json()
        new_user_name = data['userName']
        new_score = data['score']
        #return '{} {}'.format(new_user_name, new_score)
        
        result = insert_rank(new_user_name,new_score)
        if result == "Success":
            con = sqlite3.connect('MISProject_database.db')
            cur = con.cursor()
            querydata = cur.execute(f"SELECT username,userrank FROM Rank_table")
            selectResult = querydata.fetchone()
            con.close()
            if selectResult:
                return "successful insert"
            else:
                return "failed get data from DB"
        else:
            return "insert failed"
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)






