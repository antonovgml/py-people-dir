from flask import Flask, request, render_template, make_response, url_for, redirect
from flask_pymongo import PyMongo
from pprint import pprint
from peoplegen import get_random_person
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = '\x8c\xc3>\x9c\xfb\x1d\x9e[\x1f\x04\x81\x8a\xeb\xc3{Y\xfaI\x0c\xd9Doi\xea'


#MONGO_URI = 'mongodb://admin:YT%26%21b4aUYH@cluster0-shard-00-00-juobo.mongodb.net:27017,cluster0-shard-00-01-juobo.mongodb.net:27017,cluster0-shard-00-02-juobo.mongodb.net:27017/peopledir?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
MONGO_URI = 'mongodb://admin:Qwerty@10.131.35.106:27017,/peopledir?authSource=admin'

app.config['MONGO_URI'] = MONGO_URI

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
    if username: resp.set_cookie('user', username)
    return resp

@app.route("/people")	    
@app.route("/people/")	
def people():
    people = mongo.db.people.find()
    resp = make_response(render_template('people.html', people = people))
    return resp

@app.route("/people/generate")    
@app.route("/people/generate/<count>")    
def generate_person(count = '1'):
    
    try:
        count = int(count)
        for x in range(count):
            mongo.db.people.insert(get_random_person())

    except ValueError:
        pass
    
    return redirect(url_for('people'))
    
@app.route('/people/remove/<last_name>')    
@app.route('/people/remove/<last_name>/<first_name>')
def remove_people(first_name = None, last_name = None):
    filter = {}
    if first_name: 
        filter['fname'] = first_name
    if last_name: 
        filter['lname'] = last_name

    mongo.db.people.delete_many(filter)
    
    return redirect(url_for('people'))

@app.route('/people/remove/id/<id>')        
def remove_by_id(id):
    filter = {'_id': ObjectId(id)}
    mongo.db.people.delete_one(filter)
    
    return redirect(url_for('people'))    
    
@app.route('/people/update/<id>/lastname/<lname>')    
@app.route('/people/update/<id>/firstname/<fname>')
def update_person(id = None, lname = None, fname = None):

    filter = {'_id': ObjectId(id)}
    
    update = {}
    if fname:
        update['fname'] = fname
    if lname:
        update['lname'] = lname
        
    pprint({'$set':update})    
        
    result = mongo.db.people.update_one(filter, {'$set': update})    
    
    print("Modified: " + str(result.modified_count))
    
    return redirect(url_for('people'))
    
if __name__ == "__main__":
    app.run()
