from flask import Flask, request, render_template, make_response
from flask_pymongo import PyMongo
app = Flask(__name__)
app.secret_key = '\x8c\xc3>\x9c\xfb\x1d\x9e[\x1f\x04\x81\x8a\xeb\xc3{Y\xfaI\x0c\xd9Doi\xea'
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")	
@app.route("/hello/")
@app.route("/hello/<username>")
def hello(username=None):
    cookie = request.cookies.get('user')
    resp = make_response(render_template("hello.html", name=username, cookie = cookie))
    resp.set_cookie('user', username)
    return resp

if __name__ == "__main__":
    app.run()
