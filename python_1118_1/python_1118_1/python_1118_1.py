from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hellos(name=None):
    data = [dict(href="http://www.naver.com",caption="네이버"),
                dict(href="http://www.google.com",caption="구글"),
                dict(href="http://www.mixcloud.com",caption="믹스클라우드")]
    alldata = {
            'items' : data,
            'name' : 'yeachan'
            }
    return render_template('index.html', **alldata)


if __name__ == '__main__':
    app.debug = True
    app.run(host="203.252.166.51")