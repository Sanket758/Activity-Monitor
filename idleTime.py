import datetime
import sys
import json
import os
import uploader

if sys.platform == 'win32':
    from ctypes import *
     
    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_int),
        ]
         
    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0
        else:
            return 0
else:
    def get_idle_duration():
        return 0
         
def IdleCalculator():
    import time
    TotalIdleTime = 0
    TodayDate = datetime.datetime.now()  
    while 1:
        TodayDate = datetime.datetime.now()
        if(TodayDate.hour==23):
            break
        duration = get_idle_duration()
        TotalIdleTime += duration
        #print('User idle for {0:0.2f} seconds.'.format(duration))
        sys.stdout.flush()
        time.sleep(5)
    #print('Total idle time: {0:0.2f} seconds.'.format(TotalIdleTime))
    Data = {
        "Date" : TodayDate.strftime('%Y%m%d'),
        "Total_Idle_Time": TotalIdleTime
    }

    CurrentFolder = os.getcwd()
    DateInString = TodayDate.strftime('%Y%m%d')  
    fp = CurrentFolder +"\\" + DateInString
    filename = "TotalIdleTime" + DateInString + ".json"
    fullPath = fp + "\\"+ filename
    with open("{}\\{}\\TotalIdleTime{}.json".format(os.getcwd(),TodayDate.strftime('%Y%m%d'),TodayDate.strftime('%Y%m%d')),"w+")as myFile:
        json.dump(Data, myFile)
    
    FolderID = uploader.createFolder(DateInString + " json")
    uploader.UploadFile(filename,fullPath,"text/json",FolderID)
    #print("File:"+filename)
        