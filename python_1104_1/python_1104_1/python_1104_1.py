import sqlite3

con = sqlite3.connect("test.db") # connection 객체 획득

cur = con.cursor() # cursor 객체 획득 


#dropsql = '''drop table if exists phonebook;'''
#cur.execute(dropsql)

#createsql = '''create table phonebook(name text, phoneNum text);'''
#cur.execute(createsql)

#insertsql = '''insert into phonebook values('greenjoa1','010-1111-2222');'''
#cur.execute(insertsql)

#insertsql = '''insert into phonebook values('greenjoa2','010-3333-4444');'''
#cur.execute(insertsql)

#name = 'greenjoa3'
#phone = '010-5555-6666'
#insertsql = '''insert into phonebook values(?,?);''' #부분으로만 넣을 수는 없음. 부분 -> 이름을 지정해서 넣음
#cur.execute(insertsql,(name,phone))

#selectsql = '''select * from phonebook;'''
#cur.execute(selectsql)



##print(cur.fetchone())         #첫번째 (읽고 다음을 가르킴)
##print(cur.fetchall())           #현재 위치부터 끝까지 다읽음
##print(cur.fetchone())         #두번째
##print(cur.fetchone())         #다읽었으므로 없음, DB의 위치를 가르키는 포인터가 있음


#insertsql='''insert into phonebook values(?,?);''' 
#datalist=(('greenjoa4','010-4444-4444'), ('greenjoa5','010-5555-5555'))
#cur.executemany(insertsql, datalist)

#def gene():
#    datalist=(('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
#    for item in datalist:
#        yield   item
#cur.executemany(insertsql, gene())

#selectsql = '''select * from phonebook;'''
#cur.execute(selectsql)

#print(cur.fetchall())

#name = 'GREENJOA3'
#phone = '010-5555-6666'
#insertsql = '''insert into phonebook values(?,?) ''' 
#cur.execute(insertsql,(name,phone))

#def OrderFunc(str1, str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) - (s1 < s2) # 앞(음수), 같음(0), 뒤(양수)

#con.create_collation('myordering', OrderFunc)
#cur.execute("select COUNT(*) from phonebook order by name collate myordering;")
#print(cur.fetchall())
#con.commit();

dropsql = '''drop table if exists user;'''
cur.execute(dropsql)

createsql = '''create table user(name text, age int);'''
cur.execute(createsql)

insertsql = '''insert into user values('김예찬',22);'''
cur.execute(insertsql)
insertsql = '''insert into user values('황예찬',17);'''
cur.execute(insertsql)
insertsql = '''insert into user values('홍예찬',45);'''
cur.execute(insertsql)
insertsql = '''insert into user values('고예찬',7);'''
cur.execute(insertsql)
insertsql = '''insert into user values('강예찬',35);'''
cur.execute(insertsql)

class Average:
    def __init__(self):
        self.sum = 0
        self.cnt = 0

    def step(self,value): # value값이 들어오는 것에 대한 호출 
        self.sum += value
        self.cnt += 1

    def finalize(self): #최종으로 호출 되는 것 
        return self.sum / self.cnt

con.create_aggregate("avg", 1, Average) # DB에등록
cur.execute("select avg(Age) from user;")

print(cur.fetchone())
con.commit()