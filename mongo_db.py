from pymongo import *

def create_connection(hostname="localhost",portname=27017):
	global client
	client=MongoClient(hostname,portname)

def create_db(name):
	from os import mkdir
	global db
	global dbname
	db=client[name]
	dbname=name
	mkdir(dbname)
	
def add_collection(name):
	global db
	db.create_collection(name)

def add_user(name):
	from os import mkdir
	global user_list
	existing_user=False
	user_list=db.collection_names()		
	
	name=name.replace(" ","")
	for i in range(0,len(user_list)):
		user_list[i]=user_list[i].replace("u'","")
		user_list[i]=user_list[i].replace("'","")
		if(user_list[i]==name):
			existing_user=True
	
	if not existing_user:
		add_collection(name)
		mkdir(dbname+"/"+name)

def table_format(*key):
	global table_entry
	table_entry=key	

def user_data(name,*data):
	global userentry
	userentry=dict()
	name=name.replace(" ","")
	current_user=db[name]

	if(len(data)!= len(table_entry)):
		raise Exception,"Data does not match the Table Format"

	for i in range(0,len(table_entry)):
		userentry[str(table_entry[i])]=str(data[i])
		
	current_user.insert(userentry)
	
def list_users():
	for i in range(0,len(user_list)):
		user_list[i]=user_list[i].replace("u'","")
		user_list[i]=user_list[i].replace("'","")
		print(user_list[i])

create_connection()
create_db("ImageManagement")
table_format("name","age","sex","place of birth")
add_user("Rahul Saurav2")
user_data("Rahul Saurav2","Rahul Saurav",24,"Male","Bihar")
list_users()
