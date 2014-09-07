from pymongo import *
#userentry=dict()

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
	global userentry
	userentry=dict()
	for i in range(0,len(key)): 
		userentry[str(key[i])]=""

def user_data(name,*data):
	name=name.replace(" ","")
	current_user=db[name]
	count=0
	for key in userentry.keys():
		userentry[key]=str(data[count])
		count+=1
	current_user.insert(userentry)
	
userentry={"name":"unknown"}

create_connection()
create_db("ImageManagement")
table_format("name","age","sex","place of birth")
add_user("Rahul Saurav")
user_data("Rahul Saurav","Rahul Saurav",24,"Male","Bihar")

for i in range(0,100):
	username="User"+str(i)
	add_user(username)
        #collection=db[username]
	#collection.insert(userentry)	


