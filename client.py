import config.py
import menu.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

##Below code kind basic idea, probs won't work yet though##

##Dropper##
def Dropper():
    #subtract 1 to match array index at 0?
    sideLen = math.sqrt(PI_COUNT) * SCREEN_SIZE #length of a side of the whole display
    pPlace = ID * SCREEN_SIZE - SCREEN_SIZE #start position
    drops = pPlace // sideLen
    dropAmount = max(drops * SCREEN_SIZE * sideLen - 1, 0) #how much to drop, -1 zero it for array
    remainder = pPlace % sideLen #position after drop
    fPos = dropAmount + remainder #final position

	miniMap = []

	for x in range(fPos, fPos + 400): #400, idk why
	    miniMap.append(MAP[x])
	    if x == fPos + SCREEN_SIZE - 1: #might work?
	        x += 56 #+/-
	UpdateDisplayCL(miniMap)
	miniMap = []

while True:
	if not ID_Set:
		ID_Choice()
	else:
		s.bind((HOST, PORT))
		s.listen(1)
		conn, addr = s.accept()
		break
while True:
	MAP = conn.recv(4096).decode()
	Dropper()