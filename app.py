from flask import Flask, request
import sqlite3, os, sys

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
    '''
    cur.execute(f'SELECT * FROM User_table WHERE `UserMail` = "{email}"')
    queryresult = cur.fetchone
    if queryresult:
        return 'email重複,請使用另一個email'
    '''
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

def print_menuname():
    con = sqlite3.connect('MISProject_database.db')
    cur = con.cursor()
    querydata = cur.execute(f"SELECT MenuName FROM Menu_table")
    con.close
    result = querydata.fetchall()
    return result
    
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
    
@app.route('/printusername', methods=['GET', 'POST'])
def printname():
    userName = "1"
    return userName


@app.route('/printdomostmenu', methods=['GET', 'POST'])
def printmenu1():
    result = print_menuname()
    if result:
        return '{} {} {}'.format(result[0],result[1],result[2])
    else:
        return "error-menuName not found in db"
    
@app.route('/printhotmenu', methods=['GET', 'POST'])
def printhot():
    result = print_menuname()
    if result:
        return '{} {} {}'.format(result[1],result[2],result[3])
    else:
        return "error-menuName not found in db"
  
@app.route('/printAllMenu', methods=['GET', 'POST'])
def print():
    result = print_menuname()
    if result:
        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],result[14])
    else:
        return "error-menuName not found in db"
'''
@app.route('/printrelaxmenu', methods=['GET', 'POST'])
    def printrelax():
        con = sqlite3.connect('MISProject_database.db')
        cur = con.cursor()
        querydata = cur.execute(f"SELECT * FROM MenuCategory_table WHERE `CategoryName`='睡前伸展'")
        con.close
        result = querydata.fetchone()
        for row in result:
            menu1 = row[2]
            menu2 = row[3]
            menu3 = row[4]
            menu4 = row[5]
            menu5 = row[6]
        return '{} {} {} {} {}'.format(menu1,menu2,menu3,menu4,menu5)
'''        
@app.route('/test', methods=['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        email = request.form['username']
        password = request.form['password']
        return (email)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)





