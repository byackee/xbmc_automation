import xbmc,xbmcgui
import subprocess,os
 
class MyPlayer(xbmc.Player) :
 
        def __init__ (self):
            xbmc.Player.__init__(self)
 
        def onPlayBackStarted(self):
            if xbmc.Player().isPlayingVideo():
                os.system("wget --spider 'http://login:password@192.168.1.13/api/callAction?deviceID=43&name=pressButton&arg1=2 '")
 
        def onPlayBackEnded(self):
            if (VIDEO == 1):
                os.system("wget --spider 'http://login:password@192.168.1.13/api/callAction?deviceID=43&name=pressButton&arg1=1 '")
 
        def onPlayBackStopped(self):
            if (VIDEO == 1):
                os.system("wget --spider 'http://login:password@192.168.1.13/api/callAction?deviceID=43&name=pressButton&arg1=1 '")
 
        def onPlayBackPaused(self):
            if xbmc.Player().isPlayingVideo():
                os.system("wget --spider 'http://login:password@192.168.1.13/api/callAction?deviceID=43&name=pressButton&arg1=1 '")
 
        def onPlayBackResumed(self):
            if xbmc.Player().isPlayingVideo():
                os.system("wget --spider 'http://login:password@192.168.1.13/api/callAction?deviceID=43&name=pressButton&arg1=2 '")
player=MyPlayer()
 
VIDEO = 0
 
while(1):
    if xbmc.Player().isPlaying():
      if xbmc.Player().isPlayingVideo():
        VIDEO = 1
 
      else:
        VIDEO = 0
 
    xbmc.sleep(1000)