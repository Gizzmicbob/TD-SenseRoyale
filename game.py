##actual game might be?
import config
import player
import time
import funcs

curTime = time.time()

def runGame(): #does the standard game stuff
        i = 1
        #for ply in player.PlayerList:
                 #sets next spot as a player
                #config.MAP[ply.old] = config.Color0 #sets old spot as a blank spot
def GetPlayer(array):
        for ply in player.PlayerList:
                if ply.id == array[1]:
                        return ply
        return "null"

def ClearOld(ply):
        ply.old = ply.position
        config.MAP[ply.old] = config.Color0
def ReceiveKey(array):
        ply = GetPlayer(array)
        if ply != "null":
                print(ply.position)
                if array[0] == config.UP:
                        ClearOld(ply)
                        ply.position -= funcs.DropLine()
                        config.MAP[ply.position] = config.Color1
                elif array[0] == config.RIGHT:
                        ClearOld(ply)
                        ply.position += 1
                        config.MAP[ply.position] = config.Color1
                elif array[0] == config.LEFT:
                        ClearOld(ply)
                        ply.position -= 1
                        config.MAP[ply.position] = config.Color1
                elif array[0] == config.DOWN:
                        ClearOld(ply)
                        ply.position += funcs.DropLine()
                        config.MAP[ply.position] = config.Color1
        
