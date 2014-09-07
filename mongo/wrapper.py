import os
from os import chdir,mkdir
from pymongo import *

def create_connection(hostname="localhost",portname=27017):
	global client
	client=MongoClient(hostname,portname)

def create_db(name):
	global db
	global dbname
	global datapath
	db=client[name]
	dbname=name
	datapath="/home/N0maD/My_Works/MongoDB/"
	os.chdir(datapath)
	if not os.path.isdir(dbname):
		mkdir(dbname)
	
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
		os.chdir(datapath+dbname)
		mkdir(name)

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
		
	if(userentry["Photo"]!=""):
		os.chdir(datapath+dbname+"/"+name)
		cpy(userentry["Photo"],"a.jpg")
	
	current_user.insert(userentry)
	
def list_users():
	for i in range(0,len(user_list)):
		user_list[i]=user_list[i].replace("u'","")
		user_list[i]=user_list[i].replace("'","")
		print(user_list[i])

def cpy(src,dst):
	from shutil import copy2
	copy2(src,dst)

#create_connection()
#create_db("ImageManagement")
#table_format("name","age","sex","place of birth","Photo")
#add_user("Test User1")
#user_data("Test User1","Rahul Saurav",24,"Male","Bihar","/home/N0maD/Pictures/Selection_004.jpg")
#user_data("Rahul Saurav5","Rahul Saurav",24,"Male","Bihar","/home/N0maD/Pictures/Selection_005.jpg")

#list_users()
