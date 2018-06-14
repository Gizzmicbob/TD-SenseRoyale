##actual game might be?
import config.py
import player.py
import time

curTime = time.time()

def runGame(): #does the standard game stuff
	if time.time() > curTime + config.TTM:
		curTime = time.time()
		for ply in PlayerList:
			ply.position += 1 #for testing, should move right across screen... maybe?
			config.MAP[ply.position] = 1 #sets next spot as a player
			config.MAP[ply.old] = 0 #sets old spot as a blank spot
			ply.old = ply.position