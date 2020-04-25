# Activity-Monitor
Activity Monitor is an application which tracks your activities throughout the day and keeps info about it. It takes screenshot of your desktop every 5 minutes and stores it on the google drive, so user can monitor the activities done on the computer. 
This code uses google api, so you need to have credentials of your api, name it as client-secrets.json and put in the same folder as other files and you are on the go..  
check the demo on youtube: https://www.youtube.com/watch?v=YZU8rbj0s0I#action=share

# Google Drive API
Read about the API here: https://developers.google.com/drive/api/v2/about-sdk

# To get the client_secrets.json 
Go here: https://developers.google.com/drive/api/v3/quickstart/python
Press the Enable drive api button, then a dialogue box will appear, please click on Download Config, This will download a file 
named credentials.json (simply rename it to client_secrets.json)

![Image](https://github.com/Sanket758/Activity-Monitor/blob/master/Enable%20drive.png "Enable Drive")

# Install all the requirements
```
pip install -r requirements.txt
```

# Once you have everything setup run:
```
python main.py
```
