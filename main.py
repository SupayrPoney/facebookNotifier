#Dependencies: libnotify, python-gobject (or python2-gobject for Python 2) 

import fbconsole
import subprocess
import os

fbconsole.ACCESS_TOKEN = "aaa"#Put your token here

f = open('notifications.txt', 'w')
path =  os.path.dirname(os.path.realpath(__file__))

for notif in fbconsole.iter_pages(fbconsole.get("/me/notifications")):
    subprocess.call(["notify-send","From : " + notif[u'from'][u'name'],notif[u'title'] + "\n" + notif[u'link'], "--icon=" + path +"/index.jpg" ])
