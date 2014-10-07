#Dependencies: libnotify, python-gobject (or python2-gobject for Python 2) 

import fbconsole
import subprocess
import os
import time


fbconsole.AUTH_SCOPE = ['manage_notifications']
fbconsole.authenticate()

pidFile = open("pidFile.txt",'w')#Keeps the pid so it can be killed easily
pidFile.write(str(os.getpid()))
pidFile.close()

recievedNotifications = []
while(True):
    path =  os.path.dirname(os.path.realpath(__file__))

    for notif in fbconsole.iter_pages(fbconsole.get("/me/notifications")):
        print notif
        if (notif[u'id'] not in recievedNotifications):
            subprocess.call(["notify-send","From : " + notif[u'from'][u'name'],notif[u'title'] + "\n" + notif[u'link'], "--icon=" + path +"/index.jpg" ])
            recievedNotifications.append(notif[u'id'])

    time.sleep(30)