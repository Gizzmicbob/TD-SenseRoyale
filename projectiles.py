import config
import funcs
import game
import player
import time
import weapon
import random
drop = funcs.DropLine()
allProj = []
class Projectile:
        def __init__(self, direction, position, ttl, speed, accuracy):
                print("New proj" + str(position))
                #direction of new projectile
                self.direction = direction
                #position of the projectile
                self.position = position
                #old projectile position
                self.old = position
                #how long the projectile has to live
                self.ttl = ttl
                #how fast the projectile moves
                self.speed = speed
                #the accuracy of this projectile
                self.accuracy = accuracy
                #when the projectile last moved
                self.lastmove = time.time()
                #if the projectile is set to die next move
                self.toDie = False
                #buffer to avoid destroying your gun
                self.buffer = True
                #adds the projectile to the projectile list
                allProj.append(self)
        def Loss(self):
                allProj.remove(self) #removes projectile from the list
                print("Bullet lost")
                config.MAP[self.position] = config.Color0 #removes the projectile from the map
                return
        def CheckHit(self, point):
                #checks if the projectile hit a player
                #hits are based on color... might redo
                i = 0
                for col in config.PlayerColors: #if the hit point is a player color
                        if point == col:
                                game.Kill(player.PlayerList[i]) #kill the player
                        i += 1
                                
        def IsEdge(self, pos):
                #checks if you're on the edge of the map
                if pos in game.right or pos in game.left or pos in game.top or pos in game.bottom:
                        return True
        def CheckImp(self, position, direction): #use other funcs later
                change = 0 #the position change made
                if direction == 0:
                        change -= 16
                elif direction == 1:
                        change += 1
                elif direction == 2:
                        change += 16
                elif direction == 3:
                        change -= 1
                if config.MAP[position + change] == config.Color9: #if hit zone
                        self.Loss() #destroy bullet
                        return False
                elif config.MAP[position + change] != config.Color0 and config.MAP[position + change] != config.Color5 and config.MAP[position + change] != config.Color8: #nothing or gun
                        print("Projectile hit " + str(config.MAP[position + change]))
                        self.CheckHit(config.MAP[position + change]) #check player hit
                        self.toDie = True #kills projectile next
                elif self.IsEdge(position + change): #on edge
                        self.toDie = True #kills projectile next
                return True
        def AcMove(self, direction):
                #moves the player
                if direction == 0:
                        self.position -= 16
                elif direction == 1:
                        self.position += 1
                elif direction == 2:
                        self.position += 16
                elif direction == 3:
                        self.position -= 1    
                
        def Move(self):
        #calculates movement
                if time.time() > self.lastmove + self.speed: #can it move?
                        self.lastmove = time.time() #updates last move time
                        if self.toDie or self.ttl == 0: #checks if the bullet ran out of time or is set to die
                                self.Loss() #kills the bullet
                                return
                        self.ttl -= 1 #removes a point from ttl
                        #accuracy stuff
                        toMove = self.direction
                        chance = random.randint(1,100) #the rnadom number to decide if the bullet goes off course
                        if self.accuracy != 0:
                                if not chance in range(1,self.accuracy) and not self.buffer: #if inaccurate bullet and not buffered
                                        chance2 = random.randint(1,2) #which direction off course?
                                        if chance2 == 1:
                                                if self.direction == 3:
                                                        toMove = 0 #doesn't go out of range
                                                else:
                                                        toMove += 1
                                        else:
                                                if self.direction == 0:
                                                        toMove = 3 #doesn't go out of range

                                                else:
                                                        toMove -= 1
                                        if not self.CheckImp(self.position, toMove): #checks impact for this move
                                                return
                                        self.AcMove(toMove) #moves the off course direction
                        elif not self.buffer: #zero accuracy makes it melee
                                if self.direction == 0:
                                        self.direction = 3 #doesn't go out of range

                                else:
                                        self.direction -= 1 #goes left as melee attack
                        if not self.CheckImp(self.position, self.direction): #checks impact for this move
                                return
                        self.AcMove(self.direction) #moves
                        if not self.buffer:
                                config.MAP[self.old] = config.Color0 #removes old position from map
                        else:
                                self.buffer = False
                        config.MAP[self.position] = config.Color6 #sets the position to projectile color
                        self.old = self.position #updates old pos

                
