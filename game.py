##actual game might be?
import config.py
import player.py

def runGame(): #does the standard game stuff
	for ply in PlayerList:
		ply.position += 1 #for testing, should move right across screen... maybe?
		MAP[ply.position] = 1 #sets next spot as a player
		MAP[ply.old] = 0 #sets old spot as a blank spot