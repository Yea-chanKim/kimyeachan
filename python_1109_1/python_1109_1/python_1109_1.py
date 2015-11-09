import sqlite3 as sqlite

from werkzeug  import check_password_hash, generate_password_hash



def initDB():
    db = sqlite.connect("test.db")
    with open('schema.sql') as f:
        db.cursor().executescript(f.read()) # 질의문이 여러개 있는 script를 사용하기 위한 함수
        db.commit()

def getDB():
    db = sqlite.connect("test.db")
    return db

def insertData():

    db = getDB()

    print("***********회원가입***********")

    id = input("ID : ")
    name = input("Name : ")
    pw = input("Passward : ")
    
    cur = db.cursor()

    cur.execute("select * from user where userid =?",[id]) # string이므로 [] value일때만 그대로
    if(cur.fetchone() != None):
        print("아이디가 존재합니다. ")
        return
    insertsql = "insert into user(userid,username,userpw) values(?,?,?);"
    cur.execute(insertsql,[id,name, generate_password_hash(pw)])
    
    db.commit() # 넣고나서는 반드시 commit을 수행해줄 것! 다른데서 connection을 하면 다 지워짐

def login():
    db = getDB()
    cur = db.cursor()
    print()
    print("*********** 로 그 인 ***********")
    id = input("ID : ")
    pw = input("PW: ")

    cur.execute("select * from user where userid =?",[id])
    temp = cur.fetchone()
    if(temp[3] == None):
       print("아이디가 존재하지 않습니다.")
       return

    if(check_password_hash(temp[3], pw)):
       print(temp[2]+" 님 로그인 성공")
    else:
        print("실패")



initDB()

insertData()
while(True):

    login()