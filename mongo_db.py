from pymongo import *

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
	
	name=name.replace(" ","")
	for i in range(0,len(user_list)):
		user_list[i]=user_list[i].replace("u'","")
		user_list[i]=user_list[i].replace("'","")
		if(user_list[i]==name):
			existing_user=True
	
	if not existing_user:
		add_collection(name)

def table_format(*key):
	global table_entry
	table_entry=key	
	#for i in range(0,len(key)): 
	#	table_entry[i]=""

def user_data(name,*data):
	global userentry
	userentry=dict()
	name=name.replace(" ","")
	current_user=db[name]

	if(len(data)!= len(table_entry)):
		raise "The Number of Entries does not match"

	for i in range(0,len(table_entry)):
		userentry[str(table_entry[i])]=str(data[i])
		
	current_user.insert(userentry)
	
#userentry={"name":"unknown"}

create_connection()
create_db("ImageManagement")
table_format("name","age","sex","place of birth")
add_user("Rahul Saurav1")
user_data("Rahul Saurav1","Rahul Saurav",24,"Male","Bihar")

for i in range(0,100):
	username="User"+str(i)
	add_user(username)
        #collection=db[username]
	#collection.insert(userentry)	


