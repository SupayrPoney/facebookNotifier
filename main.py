#Dependencies: libnotify, python-gobject (or python2-gobject for Python 2) 

#Author : Bruno ROCHA PEREIRA


#####################  IMPORTS  #####################
import os
import time
import urllib3
import urllib2
import feedparser
import pynotify
import webbrowser



#####################  GLOBALS  #####################

RSS_STREAM = 
#INSERT YOUR RSS STREAM LINK HERE


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
    except urllib3.exceptions.MaxRetryError:
        return False

class Notifier(object):
    """docstring for Notifier"""
    def __init__(self):
        self.recievedNotifications = []
        self.getNotifications()

    def getNotifications(self):
        '''
            Gets the notifications via the Facebook API
        '''
        path = os.path.dirname(os.path.realpath(__file__))

        while(True):
            if checkInternetConnection():
                a = urllib2.urlopen(RSS_STREAM)
                b = feedparser.parse(a)
                #for i in range(len(b.entries)):
                for i in range(len(b.entries)):
                    if (b.entries[i]['id'] not in self.recievedNotifications):
                        pynotify.init("notifier")
                        n = pynotify.Notification("Notifier for Linux", b.entries[i]['title'], path + "/index.jpg")
                        n.set_hint_string('append', '')
                        n.show()
                        self.recievedNotifications.append(b.entries[i]['id'])


            time.sleep(3)

if __name__ == '__main__':
    _ = Notifier()
