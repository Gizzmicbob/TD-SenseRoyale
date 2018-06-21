##actual game might be?
import config
import player
import time
import funcs

curTime = time.time()

def runGame(): #does the standard game stuff
        for ply in player.PlayerList:
                config.MAP[ply.position] = config.Color1 #sets next spot as a player
                config.MAP[ply.old] = config.Color0 #sets old spot as a blank spot
def GetPlayer(array):
        for ply in player.PlayerList:
                if ply.id == array[1]:
                        return ply
        return "null"
                         
def ReceiveKey(array):
        ply = GetPlayer(array)
        if ply != "null":
                if array[0] == config.UP:
                        ply.old = ply.position
                        ply.position -= funcs.DropLine()
                elif array[0] == config.RIGHT:
                        ply.old = ply.position
                        ply.position += 1
                elif array[0] == config.LEFT:
                        ply.old = ply.position
                        ply.position -= 1
                elif array[0] == config.DOWN:
                        ply.old = ply.position
                        ply.position += funcs.DropLine()
        
