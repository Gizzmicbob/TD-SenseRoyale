from config import *
from menu import *
import config
import menu
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

##Below code kind basic idea, probs won't work yet though##

##Dropper##
def Dropper():
    #subtract 1 to match array index at 0?
    sideLen = math.sqrt(PI_COUNT) * SCREEN_SIZE #length of a side of the whole display
    pPlace = ID * SCREEN_SIZE - SCREEN_SIZE #start position - remember, array starts at 0
    drops = pPlace // sideLen
    dropAmount = max(drops * SCREEN_SIZE * sideLen - 1, 0) #how much to drop, -1 zero it for array
    remainder = pPlace % sideLen #position after drop
    fPos = dropAmount + remainder #final position
    miniMap = []
    for x in range(fPos, fPos + ((SCREEN_SIZE - 1) * sideLen + SCREEN_SIZE)): #400, idk why
        miniMap.append(MAP[x])
    if x == fPos + SCREEN_SIZE - 1: #might work?
        x += sideLen #+/-
        fPos = x
    UpdateDisplayCL(miniMap)
    miniMap = []

while True:
    if not config.ID_Set:
        menu.ID_Choice()
    else:
        MAP = [] #this to not have a huge map in config, and to make it automatically get a size
        for x in range(math.sqrt(PI_COUNT) * SCREEN_SIZE * 2):
            MAP.append(Color0)
        s.bind((HOST, PORT))
        conn, addr = s.accept()
        break
        print("working?")
    print(config.ID_Set)
while True:
    MAP = conn.recv(4096).decode()
    Dropper()
