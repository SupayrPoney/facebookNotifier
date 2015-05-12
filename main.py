#Dependencies: libnotify, python-gobject (or python2-gobject for Python 2) 

#Author : Bruno ROCHA PEREIRA


#####################  IMPORTS  #####################
import fbconsole
import subprocess
import os
import time
import urllib3


#####################  GLOBALS  #####################

recievedNotifications = []


###############  FACEBOOK CONNECTION  ###############

fbconsole.AUTH_SCOPE = ['manage_notifications']
fbconsole.authenticate()

###################  PID STORAGE  ###################

pidFile = open("pidFile.txt", 'w')#Keeps the pid so it can be killed easily
pidFile.write(str(os.getpid()))
pidFile.close()


#---------------------------------------------------#


def checkInternetConnection():
    '''
        Verifies if the internet connection is up and running
    '''
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', 'www.google.com')
        return True
    except urllib3.exceptions.MaxRetryError as err:
        return False


def getNotifications():
    '''
        Gets the notifications via the Facebook API
    '''
    path = os.path.dirname(os.path.realpath(__file__))

    while(True):
        if checkInternetConnection():
            for notif in fbconsole.iter_pages(fbconsole.get("/me/notifications")):
                if (notif[u'id'] not in recievedNotifications):
                    subprocess.call(["notify-send", "From : " + notif[u'from'][u'name'],notif[u'title'] + "\n" + notif[u'link'], "--icon=" + path +"/index.jpg" ])
                    recievedNotifications.append(notif[u'id'])

        time.sleep(30)


if __name__ == '__main__':
    getNotifications()
