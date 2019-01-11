import datetime
import os
import time

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import client, file, tools

from Authenticator import Authenticate

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

DRIVE=Authenticate()

def createFolder(name):
	file_metadata = {
        'title': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
	file = DRIVE.files().insert(body=file_metadata,fields='id').execute()
	return file.get('id')

def UploadFile(fileName,filePath,mimeType,FolderId):
	file_metadata = {'title': fileName,'parents': [{'id':FolderId}]}
	media = MediaFileUpload(filePath,mimetype=mimeType)
	file = DRIVE.files().insert(body=file_metadata,media_body=media,fields='id').execute()
