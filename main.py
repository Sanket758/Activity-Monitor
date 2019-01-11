import datetime
import getpass
import os
import shutil
import sys
import time
from threading import Thread

import schedule

import idleTime
import ss
#import Startup
import winshell
from win32com.client import Dispatch

TodayDate = datetime.datetime.now()


def start():
    Thread(target = ss.TakeSS).start()
    Thread(target = idleTime.IdleCalculator).start()

def CleanUp():
    a = os.getcwd()
    fp = a+"\\"+TodayDate.strftime('%Y%m%d')
    shutil.rmtree(fp, ignore_errors=True)
   
if (TodayDate.hour>9 and TodayDate.hour<23):
    start()
else:
    print("will start next day..................")


#Current = os.getcwd()
#FilePath = Current + '\\' + 'main.exe'
#Startup.add_to_startup(FilePath)
USER_NAME = getpass.getuser()

st_path = r'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % USER_NAME

path = os.path.join(st_path, "Activity Monitor.lnk")
target = os.getcwd()+"\\"+"main.exe"
wDir = os.getcwd()
icon = os.getcwd()+"\\"+"main.exe"
 
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

schedule.every().day.at("09:00").do(start)
schedule.every().day.at("23:02").do(CleanUp)


while 1:
    schedule.run_pending()
    time.sleep(1)
