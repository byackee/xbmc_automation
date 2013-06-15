import xbmc,xbmcgui
import subprocess,os
import time

IDLE = 0
DIDPLAY = 0
IDLETIME = 360
while(1):
    if (xbmc.getGlobalIdleTime() > IDLETIME):
        if (IDLE == 0) and (DIDPLAY == 0):
            os.system("wget --spider 'http://login:password@192.168.1.1/api/callAction?deviceID=70&name=turnOff'")
            IDLE = 1
        elif(DIDPLAY == 1) and ((time.time() - lastcheck) > IDLETIME):
            DIDPLAY = 0;
    else:
		os.system("wget --spider 'http://login:password@192.168.1.1/api/callAction?deviceID=70&name=turnOn'")
		IDLE = 0
    if (xbmc.Player().isPlaying() == 1):
        IDLE = 0
        DIDPLAY = 1
        lastcheck = time.time()
    xbmc.sleep(3000)