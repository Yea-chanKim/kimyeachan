from flask import Flask, url_for,redirect

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_world(user):
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Login"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '203.252.166.51',port = 5000)