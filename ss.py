import datetime
import os
import sys
import time

import pyautogui
import schedule

import uploader


def TakeSS():
    TodayDate = datetime.datetime.now()
    FolderID = uploader.createFolder(TodayDate.strftime('%Y%m%d'))
    while 1:
        TodayDate = datetime.datetime.now()  
        if (TodayDate.hour==23):
            break
        CurrentFolder = os.getcwd()
        fp = CurrentFolder +"\\" + TodayDate.strftime('%Y%m%d')
        if os.path.exists(fp):
            pass
        else:
            os.mkdir(fp)
        # Take screensot
        pic = pyautogui.screenshot()
        #Name the file with data and time
        ts = time.strftime("%Y%m%d-%H%M%S")
        filename = "screenshot"
        filename += str(ts)
        filename += ".jpg"
        # Save the image
        with open("{}\\{}".format(fp,filename),"w+")as myFile:
            pic.save(myFile)
        fullPath = fp + "\\"+ filename
        uploader.UploadFile(filename,fullPath,"image/png",FolderID)

        time.sleep(300)