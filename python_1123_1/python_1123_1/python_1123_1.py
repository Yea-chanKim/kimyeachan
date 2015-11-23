import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from contextlib import closing # 문서 닫을 때 자동으로 닫아주는것

# configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key' # session 개체를 사용하기 위한것
USERNAME = 'admin'
PASSWORD = '1234'

app = Flask(__name__) # flask 생성 
app.config.from_object(__name__) #flask app의 환경설정을 할 수 있다.(대문자)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    db = connect_db()
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.before_request # 가장 먼저 호출 -> 디비 열기
def before_request():
    g.db = connect_db() # 다른 web page에서도 사용하기 위해 전역으로 생성


@app.teardown_request #마지막으로 호출 -> 디비 닫기, 
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('SELECT title,text FROM entries ORDER BY id desc;')
    entries = [dict(title=row[0],text = row[1]) for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html', entries=entries) 


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/add' , methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title,text) values(?,?)',[request.form['title'],request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/logut')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.run(host="203.252.166.51")