import config
import menu
import socket
import display
import math
import networking
import resource
import funcs
import curses
import threading

scr = curses.initscr()
def GetInput():
        while True:
                key = scr.getch()
                if key != -1:
                    networking.SendSVR(key, config.ControllerID)

def Control():
    print("banana")

######Client Code######
resource.setrlimit(
    resource.RLIMIT_CORE,
    (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

##Below code kind basic idea, probs won't work yet though##

while True:
    if not config.ID_Set:
        menu.ID_Choice()
    else:
        config.MAP = [] #this to not have a huge map in config, and to make it automatically get a size
        for x in range(int(config.PI_COUNT * config.SCREEN_SIZE * config.SCREEN_SIZE)):
                config.MAP.append(config.Color0)
        break
        print("working?")

def main():
        while True:
            config.MAP = networking.ReceiveCL()

InputThread = threading.Thread(target=GetInput)
InputThread.start()
MainThread = threading.Thread(target=main)
MainThread.start()
