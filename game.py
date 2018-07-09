##actual game might be?
import config
import player
import time
import funcs
import math
import projectiles
import weapon

#put these in config since they are used multiple times

sideLen = config.SIDELEN
#collect sides
top = []
right = []
bottom = []
left = []
curTime = time.time()
GameOver = False
zonePoint = -1
zoneDirection = 1
GameWin = config.Color0
def GameStart():
        #sets the initial values
        global GameOver
        global curTime
        global zonePoint
        global zoneDirection
        global GameWin
        curTime = time.time()
        GameOver = False
        zonePoint = -1
        zoneDirection = 1
        GameWin = config.Color0
for i in range(sideLen):
        #might not work on larger scale - have to test more
        top.append(i)
        bottom.append(i + (sideLen * sideLen - sideLen))
        right.append(i * sideLen + sideLen - 1)
        left.append(i * sideLen)
def runGame(): #does the standard game stuff
        for i in projectiles.allProj:
                #moves all active projectiles
                i.Move()
        for ply in player.PlayerList:
                #checks every player's animation - optimize later?
                ply.Reload(RenderPlayer)
        CloseZone() #continue closing the zone
def GetPlayer(array):
        #gets the player for another function
        for ply in player.PlayerList:
                if ply.id == array:
                        return ply
        return "null"
def ClearOld(ply):
        #clears the player's old position on the map
        ply.old[0] = ply.body1
        ply.old[1] = ply.body2
        ply.old[2] = ply.wep1
        ply.old[3] = ply.wep2
        for x in ply.old:
                config.MAP[x] = config.Color0
def IsEdge(ply, direction):
        bod = [ply.body1, ply.body2, ply.wep1, ply.wep2] #the player body in an array to loop it
        #checks map edge impacts
        for x in bod:
                print(x)
                if x in right and direction == 1:
                        print("Someone hit the right edge")
                        return True
                elif x in left and direction == 3:
                        print("Someone hit the left edge")
                        return True
                elif x in top and direction == 0:
                        print("Someone hit the top edge")
                        return True
                elif x in bottom and direction == 2:
                        print("Someone hit the bottom edge")
                        return True
        return False
def RenderPlayer(ply):
        if config.MAP[ply.body1] == config.Color9 or config.MAP[ply.body2] == config.Color9  or config.MAP[ply.wep1] == config.Color9  or config.MAP[ply.wep2] == config.Color9:
                return
        ClearOld(ply)
        #renders the player's current position on the map
        curWep = ply.curwep #the player's current weapon
        play = player.PlayerList.index(ply) #index of the player
        if 1 > len(config.MAP):
                print("Map seems empty")
                return #return if map is nonexistent
        try:
                #renders player and their gun... gun color based on the weapon they are using
                if ply.alive:
                        config.MAP[ply.body1] = config.PlayerColors[play]
                        config.MAP[ply.body2] = config.PlayerColors[play]
                        config.MAP[ply.wep1] = ply.wep1col
                        config.MAP[ply.wep2] = ply.wep2col
        except:
                print("Map Array Size - " + str(len(config.MAP)))
                print("Body1 Pos - " + str(ply.body1))
def DeathRender(ply):
        #renders the player after death
        if config.MAP[ply.body1] != config.Color9:
                config.MAP[ply.body1] = config.Color7
        if config.MAP[ply.body2] != config.Color9:
                config.MAP[ply.body2] = config.Color7
        if config.MAP[ply.wep1] != config.Color9:
                config.MAP[ply.wep1] = config.Color7
        if config.MAP[ply.wep2] != config.Color9:
                config.MAP[ply.wep2] = config.Color7
def EndGame():
        #runs endgame stuff
        global GameWin
        global GameOver
        ply = 0
        #find the last player
        for pl in player.PlayerList:
                ply = pl
                break
        plIn = player.PlayerList.index(ply)
        plWIn = config.PlayerColors[plIn]
        print(str(plWIn) + " won the game!") #tells which color won
        GameWin = plWIn #sets the win color
        GameOver = True
def Kill(ply):
        ply.alive = False #sets the player to dead
        DeathRender(ply) #does the final render for the player
        print("Someone died") #nuff said?
        del config.PlayerColors[player.PlayerList.index(ply)] #removes they color
        player.PlayerList.remove(ply) #removes the player
        if len(player.PlayerList) == 1: #ends the game if the last player is alive
                EndGame()
#blue zone sutff
def CloseZone():
        global curTime
        global zonePoint
        global zoneDirection
        if curTime + config.ZoneSpeed < time.time(): #if enough time has passed to move zone
                curTime = time.time() #resets timer
                #if its direction, moves forward and changes direction if necessary
                if zoneDirection == 1:
                        zonePoint += 1
                        if zonePoint in right or config.MAP[zonePoint + 1] == config.Color9:
                                zoneDirection = 2
                elif zoneDirection == 2:
                        zonePoint += funcs.DropLine()
                        if zonePoint in bottom or config.MAP[zonePoint + funcs.DropLine()] == config.Color9:
                                zoneDirection = 3
                elif zoneDirection == 3:
                        zonePoint -= 1
                        if zonePoint in left or config.MAP[zonePoint - 1] == config.Color9:
                                zoneDirection = 0
                elif zoneDirection == 0:
                        zonePoint -= funcs.DropLine()
                        if zonePoint in top or config.MAP[zonePoint - funcs.DropLine()] == config.Color9:
                                zoneDirection = 1
        #kills player if the player is in the zone
        if config.MAP[zonePoint] in config.PlayerColors:
                peep = player.PlayerList[config.PlayerColors.index(config.MAP[zonePoint])] #get the player the zone hit
                Kill(peep)
        config.MAP[zonePoint] = config.Color9 #sets the current point to the zone                           
def MoveBod(ply, direction):
        #if the player rotates into the zone, kills them
        if config.MAP[ply.wep1] == config.Color9 or config.MAP[ply.wep2] == config.Color9:
                Kill(ply)
                return False
        ClearOld(ply)
        #rotates the player to the correct direction
        if direction == 0:
               ply.Up()
        elif direction == 1:
               ply.Right()
        elif direction == 2:
                ply.Down()
        else:
                ply.Left()
        ply.direction = direction #sets the new direction to the player
        RenderPlayer(ply) #renders the player after turning
        return True
def PosCheck(position, direction):
        #checks collisions from base position
        if direction == 0:
                return [position, position - 1]
        elif direction == 1:
                return [position, position + funcs.DropLine()]
        elif direction == 2:
                return [position + funcs.DropLine(), position + funcs.DropLine() - 1]
        elif direction == 3:
                return [position - 1, position - 1 + funcs.DropLine()]
                
def NextClear(position, direction):
        #checks if the next position is clear
        x,y = PosCheck(position, direction)
        if config.MAP[x] == config.Color0 and config.MAP[y] == config.Color0:
                return True
        return False
def Collision(ply, position, direction, npos):
        if ply.direction != direction:
                #rotates if not facing that direction
                if not MoveBod(ply, direction):
                        return True
                return False
        #doesn't allow you to move out of the array size
        if position + funcs.DropLine() >= len(config.MAP):
                return True
        #checks next pos
        elif not NextClear(position, direction):
                return True
        #check edge hit
        elif IsEdge(ply, direction):
                return True
        ClearOld(ply) #clears old pos
        ply.SetPos(npos) #sets the new pos
        return False
def NegNum(number):
        #returns the opposite of the number
        number *= -1
        return number
def ReceiveKey(array): #find a neater way to do this
        ply = GetPlayer(array[1]) #finds the player
        if ply != "null":
                #clears old position and renders the player if there is no collision
                if array[0] == config.UP:
                        if not Collision(ply, ply.position - funcs.DropLine(), 0, NegNum(funcs.DropLine())):
                                #ClearOld(ply)
                                RenderPlayer(ply)
                elif array[0] == config.RIGHT:
                        if not Collision(ply, ply.position + 1, 1, 1):
                                #ClearOld(ply)
                                RenderPlayer(ply)
                elif array[0] == config.LEFT:
                        if not Collision(ply, ply.position - 1, 3, NegNum(1)):
                                #ClearOld(ply)
                                RenderPlayer(ply)
                elif array[0] == config.DOWN:
                        if not Collision(ply, ply.position + funcs.DropLine(), 2, 16):
                                #ClearOld(ply)
                                RenderPlayer(ply)
                elif array[0] == config.SHOOT:
                        #shoots
                       ply.Shoot(PosCheck)
                elif array[0] == config.CHANGE:
                        #changes your weapon
                        print("A player changed weapon")
                        ply.weapon += 1
                        #ensures you never excede the weapon count
                        if ply.weapon > len(weapon.WeaponList) - 1:
                                ply.weapon = 0
                        ply.ChangeWep() #changes the weapon visual
                        RenderPlayer(ply) #renders the player
