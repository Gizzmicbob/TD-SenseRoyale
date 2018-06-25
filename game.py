##actual game might be?
import config
import player
import time
import funcs
import math

curTime = time.time()
#put these in config since they are used multiple times
square = math.sqrt(config.PI_COUNT)
sideLen = int(square * config.SCREEN_SIZE)
#collect sides
top = []
right = []
bottom = []
left = []
for i in range(sideLen):
        top.append(i)
        bottom.append(i + (sideLen * sideLen - sideLen))
        right.append(i * sideLen + 15)
        left.append(i * 16)
        print(right[i])

def runGame(): #does the standard game stuff
        i = 1
        #for ply in player.PlayerList:
                 #sets next spot as a player
                #config.MAP[ply.old] = config.Color0 #sets old spot as a blank spot
def GetPlayer(array):
        for ply in player.PlayerList:
                if ply.id == array:
                        return ply
        return "null"

def ClearOld(ply):
        ply.old = ply.position
        config.MAP[ply.old] = config.Color0
def IsEdge(ply, position):
        if ply.position in right and position == ply.position + 1:
                print("edgy1")
                return True
        elif ply.position in left and position == ply.position - 1:
                print("edgy2")
                return True
        elif ply.position in top and position == ply.position - funcs.DropLine():
                print("edgy3")
                return True
        elif ply.position in bottom and position == ply.position + funcs.DropLine():
                print("edgy4")
                return True
        return False
def Collision(ply, position):
        print(position)
        if position >= len(config.MAP):
                return True
        elif config.MAP[position] != config.Color0:
                return True
        elif IsEdge(ply, position):
                return True
        return False
def ReceiveKey(array): #find a neater way to do this
        ply = GetPlayer(array[1])
        if ply != "null":
                print(ply.position)
                if array[0] == config.UP:
                        if not Collision(ply, ply.position - funcs.DropLine()):
                                ClearOld(ply)
                                ply.position -= funcs.DropLine()
                                config.MAP[ply.position] = config.Color1
                elif array[0] == config.RIGHT:
                        if not Collision(ply, ply.position + 1):
                                ClearOld(ply)
                                ply.position += 1
                                config.MAP[ply.position] = config.Color1
                elif array[0] == config.LEFT:
                        if not Collision(ply, ply.position - 1):
                                ClearOld(ply)
                                ply.position -= 1
                                config.MAP[ply.position] = config.Color1
                elif array[0] == config.DOWN:
                        if not Collision(ply, ply.position + funcs.DropLine()):
                                ClearOld(ply)
                                ply.position += funcs.DropLine()
                                config.MAP[ply.position] = config.Color1
        
