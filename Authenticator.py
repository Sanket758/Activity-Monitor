from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload
import argparse
import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def Authenticate():
	try:
		flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
	except ImportError:
		flags = None
	SCOPES = 'https://www.googleapis.com/auth/drive'
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets(find("client_secret.json", '/'), scope=SCOPES)
		creds = tools.run_flow(flow, store)
	try:
		DRIVE = build('drive', 'v2', http=creds.authorize(Http()))
	except:
		print("Error occured")
	return DRIVE		

