##actual game might be?
import config
import player
import time

curTime = time.time()

def runGame(): #does the standard game stuff
        for ply in player.PlayerList:
                #print(config.MAP)
                config.MAP[ply.position] = config.Color1 #sets next spot as a player
                #config.MAP[ply.old] = config.Color0 #sets old spot as a blank spot

        """global curTime
        if time.time() > curTime + config.TTM:
                curTime = time.time()
                for ply in player.PlayerList:
                        ply.position += 1 #for testing, should move right across screen... maybe?
                        config.MAP[ply.position] = config.Color1 #sets next spot as a player
                        config.MAP[ply.old] = config.Color0 #sets old spot as a blank spot
                        ply.old = ply.position"""
