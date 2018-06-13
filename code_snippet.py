##old##
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import networking.py
import random
import time
import socket

sense = SenseHat()
ID = 0
tempID = 0
IDed = False
textSpeed = 0.04

unPressed = True

Checked = 0
Mode = "Client"

HOST = '224.0.0.1'
PORT = 27030

def disID():
    sense.show_message(str(tempID), textSpeed)
def disMode():
    sense.show_message(str(tempID), textSpeed)
        
def checkID():
    global ID
    global tempID
    global IDed
    global unPressed
    global Checked
    global Mode
    if Checked == 0:
        sense.show_message(str(tempID), textSpeed)
    elif Checked == 1:
        sense.show_message(Mode, textSpeed)
    for event in sense.stick.get_events():
        print(Checked)
        if event.action == "released":
            unPressed = True
            return
        if not unPressed:
            return
        unPressed = False
        if event.direction == "middle":
            if Checked == 0:
                ID = tempID
                IDed = True
                Checked = 1
            elif Checked == 1:
                Checked = 2
        elif event.direction == "right":
            if Checked == 0:
                tempID += 1
            else:
                Mode = "Client"
        elif event.direction == "left":
            if Checked == 0:
                tempID -= 1
            else:
                Mode = "Server"

def Server()
    
            
Players = "test"
temp = False
while True:
    if Checked < 2:
        checkID()
    else:
        print(Mode)
        if Mode == "Server":
            #if not temp:
            #    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            #        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
            #        s.sendto(Players.encode(), (HOST,PORT))
            #data, addr = socket.recvfrom(1024)
            Server()
            print(Mode)
        elif Mode == "Client":
            sense.show_message("a" + str(ID), textSpeed)

##Dropper##
def Dropper():
    #subtract 1 to match array index at 0?
    sideLen = math.sqrt(PI_COUNT) * SCREEN_SIZE #length of a side of the whole display
    pPlace = ID * SCREEN_SIZE - SCREEN_SIZE #start position
    drops = pPlace // sideLen
    dropAmount = max(drops * SCREEN_SIZE * sideLen - 1, 0) #how much to drop, -1 zero it for array
    remainder = pPlace % sideLen #position after drop
    fPos = dropAmount + remainder #final position
    return fPos

##Decompiler##
miniMap = []
Count = Dropper()
for x in range(Count, Count + 400): #400, idk why
    miniMap.append(MAP[x])
    if x == Count + SCREEN_SIZE - 1: #might work?
        x += 56 #+/-
UpdateDisplay()
miniMap = []
