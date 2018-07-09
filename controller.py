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
import pickle
import sys

scr = curses.initscr()
def GetInput():
        #gets keys forever and sends to server
        while True:
                key = scr.getch()
                if key != -1:
                    networking.SendSVR(key, config.ControllerID)

######Client Code######
#not required?
resource.setrlimit(
    resource.RLIMIT_CORE,
    (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

while True:
    if not config.ID_Set:
        menu.ID_Choice() #if ID isn't set, keep trying
    else:
        #generate map
        config.MAP = []
        for x in range(int(config.PI_COUNT * config.SCREEN_SIZE * config.SCREEN_SIZE)):
                config.MAP.append(config.Color0)
        config.DPS(sys.getsizeof(pickle.dumps(config.MAP)))
        break

def main():
        #keep receiving from server
        while True:
            config.MAP = networking.ReceiveCL()

#threads for multitasking
InputThread = threading.Thread(target=GetInput)
InputThread.start()
MainThread = threading.Thread(target=main)
MainThread.start()
