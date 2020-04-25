# Importing all the required packages
# These packages can be installed using requirements.txt (instructions are provided in readme
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload
import argparse
import os

# This function will find a specific file in given path
# this is needed when you want to find any file in your systems directory
# takes two arguments: 1:name of the file you want to find, 2: path to the directory in which you want to find
# returns the full path for that file... 
def find(name, path):
    for root, dirs, files in os.walk(path): 
        if name in files:
            return os.path.join(root, name) #this will join the file name with its path (for ex. home/usr/bin/abc.txt , where abc.txt is filename)

# This function is used to aunthenticate the user.
# We are using google drive so we have to first aunthenticate our http request before making any uploads
# obviously right?, you dont want any one to upload to your drive
def Authenticate():
	# Don't bother about the following code, its used when you are providing argument, but we won't do it
	try:
		flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
	except ImportError:
		flags = None
	
	# Scopes are the permissions for this particular app
	# if you want full permissions which includes, list/upload/download/delete files on your drive then use following scope
	# There are other scopes as well like read-only, Read more here: https://developers.google.com/drive/api/v2/about-auth
	SCOPES = 'https://www.googleapis.com/auth/drive' #in my case i am provide full access
	
	# After authentication is successful, it will create a token.json file which includes your login info
	store = file.Storage('token.json')
	
	# This line will load token.json into creds variable
	creds = store.get()
	
	# When you are running this script for the first time, you won't have token.json right...this will create it 
	if not creds or creds.invalid:
		# This will find client_secrets file from your directory 
		# '/' means root directory, it's not compulsory to have this file in your project folder
		# If you don't know what client_secret means plz read README.MD
		flow = client.flow_from_clientsecrets(find("client_secret.json", '/'), scope=SCOPES)
		# This line will create a token for you and store it in your system, and load it in creds variable
		creds = tools.run_flow(flow, store)
	
	# Now finally This code will authenticate you and creates http session and stores it in your Drive object
	# This drive object is important because you will need it to all the stuff
	try:
		DRIVE = build('drive', 'v2', http=creds.authorize(Http()))
	except:
		print("Error occured")
		
	return DRIVE		

