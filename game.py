##actual game might be?
import config
import player
import time
import funcs
import math
import projectiles

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
        for i in projectiles.allProj:
                i.Move()
        #for ply in player.PlayerList:
                 #sets next spot as a player
                #config.MAP[ply.old] = config.Color0 #sets old spot as a blank spot
def GetPlayer(array):
        for ply in player.PlayerList:
                if ply.id == array:
                        return ply
        return "null"

def ClearOld(ply):
        ply.old[0] = ply.body1
        ply.old[1] = ply.body2
        ply.old[2] = ply.wep1
        ply.old[3] = ply.wep2
        for x in ply.old:
                config.MAP[x] = config.Color0
        """config.MAP[ply.old] = config.Color0
        config.MAP[ply.old - 1] = config.Color0
        config.MAP[ply.old + funcs.DropLine()] = config.Color0
        config.MAP[ply.old + funcs.DropLine() - 1] = config.Color0"""
def IsEdge(ply, direction):
        bod = [ply.body1, ply.body2, ply.wep1, ply.wep2]
        for x in bod:
                print(x)
                if x in right and direction == 1:
                        print("edgy1")
                        return True
                elif x in left and direction == 3:
                        print("edgy2")
                        return True
                elif x in top and direction == 0:
                        print("edgy3")
                        return True
                elif x in bottom and direction == 2:
                        print("edgy4")
                        return True
        return False
def RenderPlayer(ply):
        config.MAP[ply.body1] = config.Color1
        config.MAP[ply.body2] = config.Color1
        if ply.weapon == 0:
                config.MAP[ply.wep1] = config.Color5
                config.MAP[ply.wep2] = config.Color5
"""def SwitchDir(ply, direction):
        if ply.direction == 0:
                #dirs = [ply.position, ply.]"""
def MoveBod(ply, direction):
        print(direction)
        if direction == 0:
               player.Up(ply)
        elif direction == 1:
               player.Right(ply)
        elif direction == 2:
                player.Down(ply)
        else:
                player.Left(ply)
        ply.direction = direction
def PosCheck(position, direction):
        #checks collisions from base position
        #config.MAP[position] = config.Color3
        if direction == 0:
                return [position, position - 1]
        elif direction == 1:
                return [position, position + funcs.DropLine()]
        elif direction == 2:
                return [position + funcs.DropLine(), position + funcs.DropLine() - 1]
        elif direction == 3:
                return [position - 1, position - 1 + funcs.DropLine()]
                
def NextClear(position, direction):
        x,y = PosCheck(position, direction)
        #print(x)
        #print(y)
        if config.MAP[x] == config.Color0 and config.MAP[y] == config.Color0:
                #("eek")
                return True
        return False
def Collision(ply, position, direction, npos):
        #print(position)
        if ply.direction != direction:
                ClearOld(ply)
                #ply.SetPos(npos)
                MoveBod(ply, direction)
                return False
        if position + funcs.DropLine() >= len(config.MAP):
                return True
        elif not NextClear(position, direction):
                return True
        elif IsEdge(ply, direction):
                return True
        ClearOld(ply)
        ply.SetPos(npos)
        return False
def NegNum(number):
        number *= -1
        return number
def ReceiveKey(array): #find a neater way to do this
        ply = GetPlayer(array[1])
        if ply != "null":
                #print(ply.position)
                if array[0] == config.UP:
                        if not Collision(ply, ply.position - funcs.DropLine(), 0, NegNum(funcs.DropLine())):
                                ClearOld(ply)
                                #ply.position -= funcs.DropLine()
                                #ply.SetPos(NegNum(funcs.DropLine()))
                                RenderPlayer(ply)
                                #config.MAP[ply.position] = config.Color1
                elif array[0] == config.RIGHT:
                        if not Collision(ply, ply.position + 1, 1, 1):
                                ClearOld(ply)
                                #ply.position += 1
                                #config.MAP[ply.position] = config.Color1
                                #ply.SetPos(1)
                                RenderPlayer(ply)
                elif array[0] == config.LEFT:
                        if not Collision(ply, ply.position - 1, 3, NegNum(1)):
                                ClearOld(ply)
                                #ply.position -= 1
                                #config.MAP[ply.position] = config.Color1
                               # ply.SetPos(NegNum(1))
                                RenderPlayer(ply)
                elif array[0] == config.DOWN:
                        if not Collision(ply, ply.position + funcs.DropLine(), 2, 16):
                                ClearOld(ply)
                                #ply.position += funcs.DropLine()
                                #config.MAP[ply.position] = config.Color1
                               # ply.SetPos(16)
                                RenderPlayer(ply)
                elif array[0] == config.SHOOT:
                        x = 0
                        if ply.direction == 1 or ply.direction == 2:
                                x = 1
                        if ply.weapon == 0:
                                projectiles.Projectile(ply.direction, PosCheck(ply.position, ply.direction)[x], 5, 1)
                        elif ply.weapon == 1:
                                projectiles.Projectile(ply.direction, PosCheck(ply.position, ply.direction)[x], 30, 0)
                        elif ply.weapon == 2:
                                projectiles.Projectile(ply.direction, PosCheck(ply.position, ply.direction)[x], 1, 0)
                elif array[0] == config.CHANGE:
                        ply.weapon += 1
                        if ply.weapon > 2:
                                ply.weapon = 0
        
                        
