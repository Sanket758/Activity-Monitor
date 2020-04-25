# System library imports
import datetime
import os
import time

# Third party imports
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import client, file, tools

#importing our aunthenticator, before uploading we will first aunthenticate user
from Authenticator import Authenticate

# Don't bother
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# This will run authentic method, if you dont have a token it will generate one for you
# Stores the returned object with your login info in DRIVE variable(if aunthentication is successful)
DRIVE=Authenticate()

# If Want to create a folder on your drive before doing a staright upload then call this function
# Arguments: name- name of the folder to create
# returns: creates a folder with given name on your google drive and return a ID of that folder (This id will be needed later at the time of uploading)
def createFolder(name):
	file_metadata = {
        'title': name,
        'mimeType': 'application/vnd.google-apps.folder'
    	} # create metadata for your folder
	# This code uses drive object to insert(create) a new folder in your drive
	file = DRIVE.files().insert(body=file_metadata,fields='id').execute()
	return file.get('id') # returns the id for this folder

# This function is for uploading file
# Takes 4 arguments:
# 1. filename - name of the file 2. Path - directory path of your file
# 3. mimetype- type of file you wanna upload (for ex:  'image/png' or 'image/jpg')\
# 4. FolderID - ID of the folder you get whene createFolder() is called. 
def UploadFile(fileName,filePath,mimeType,FolderId):
	file_metadata = {'title': fileName,'parents': [{'id':FolderId}]} #creates metadata object for your file
	media = MediaFileUpload(filePath,mimetype=mimeType) # This is the method from GDrive API to uploade files
	file = DRIVE.files().insert(body=file_metadata,media_body=media,fields='id').execute() # finally executes the quere which uploads your file
