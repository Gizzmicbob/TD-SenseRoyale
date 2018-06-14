##actual game might be?
import config.py
import player.py
import time

curTime = time.time()

def runGame(): #does the standard game stuff
	if time.time() > curTime + TTM:
		curTime = time.time()
		for ply in PlayerList:
			ply.position += 1 #for testing, should move right across screen... maybe?
			MAP[ply.position] = 1 #sets next spot as a player
			MAP[ply.old] = 0 #sets old spot as a blank spot
			ply.old = ply.position