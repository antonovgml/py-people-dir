from pymongo import MongoClient
import datetime
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
MONGO_URL = 'mongodb://admin:YT%26%21b4aUYH@cluster0-shard-00-00-juobo.mongodb.net:27017,cluster0-shard-00-01-juobo.mongodb.net:27017,cluster0-shard-00-02-juobo.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
# "mongodb://[admin:YT&!b4aUYH@]host1[:port1]"
client = MongoClient(MONGO_URL)

jdoe = {
    "fname": "John",
	"lname": "Doe",
	"birthdate": datetime.datetime(1980, 5, 15, 0, 0, 0)
}

bsmith = {
    "fname": "Bill",
	"lname": "Smith",
	"birthdate": datetime.datetime(1990, 10, 20, 0, 0, 0)
}





db=client.admin
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)

db = client.peopledir
people_coll = db.people
people_coll.insert(jdoe) 
people_coll.insert(bsmith)

for pers in people_coll.find():
  pprint(pers)


#db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)