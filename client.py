import config
import menu
import socket
import display
import math

##Below code kind basic idea, probs won't work yet though##

##Dropper##
def Dropper():
    #subtract 1 to match array index at 0?
    sideLen = math.sqrt(config.PI_COUNT) * config.SCREEN_SIZE #length of a side of the whole display
    pPlace = config.ID * config.SCREEN_SIZE - config.SCREEN_SIZE #start position - remember, array starts at 0
    drops = pPlace // sideLen
    dropAmount = max(drops * config.SCREEN_SIZE * sideLen - 1, 0) #how much to drop, -1 zero it for array
    remainder = pPlace % sideLen #position after drop
    fPos = dropAmount + remainder #final position
    miniMap = []
    for x in range(fPos, fPos + ((config.SCREEN_SIZE - 1) * sideLen + config.SCREEN_SIZE)): #400, idk why
        miniMap.append(config.MAP[x])
    if x == fPos + config.SCREEN_SIZE - 1: #might work?
        x += sideLen #+/-
        fPos = x
    display.UpdateDisplayCL(miniMap)
    miniMap = []

while True:
    if not config.ID_Set:
        menu.ID_Choice()
    else:
        config.MAP = [] #this to not have a huge map in config, and to make it automatically get a size
        for x in range(int(config.PI_COUNT * config.SCREEN_SIZE)):
                config.MAP.append(config.Color0)
        s.bind((config.HOST, config.PORT))
        #conn, addr = s.accept()
        break
        print("working?")
while True:
    config.MAP = networking.ReceiveCL()
    Dropper()
