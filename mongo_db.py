from pymongo import *
userentry=dict()

def create_connection(hostname="localhost",portname=27017):
	global client
	client=MongoClient(hostname,portname)

def create_db(name):
	global db
	db=client[name]
	
def add_collection(name):
	global db
	db.create_collection(name)

def add_user(name):
	global user_list
	existing_user=False
	user_list=db.collection_names()		
	
	for i in range(0,len(user_list)):
		user_list[i]=user_list[i].replace("u'","")
		user_list[i]=user_list[i].replace("'","")
		if(user_list[i]==name):
			existing_user=True
	
	if not existing_user:
		add_collection(name)

def table_format():
	global userentry
	
userentry={"name":"unknown"}

create_connection()
create_db("ImageManagement")
for i in range(0,100):
	username="User"+str(i)
	add_user(username)
        collection=db[username]
	#collection.insert(userentry)	


