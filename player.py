#import funcs
PlayerList = []
import time
import funcs
import config
import weapon
import projectiles
drop = funcs.DropLine()       

class Player:
        ###important - integrate with funcs###
        def __init__(self, position, ID):
                self.position = position #the base player pos
                #the body part positions
                self.body1 = position
                self.body2 = position - 1
                self.wep1 = position + drop
                self.wep2 = position + drop - 1
                #player's old positions
                self.old = [self.body1, self.body2, self.wep1, self.wep2]
                #current weapon
                self.weapon = 0
                #the current weapon class
                self.curwep = weapon.WeaponList[self.weapon]
                #dead or alive
                self.alive = True
                #player id
                self.id = ID
                #currently reloading or not
                self.reloading = False
                #weapon colors
                self.wep1col = self.curwep.wep1
                self.wep2col = self.curwep.wep2
                #the player direction
                self.direction = 0
                #when the player last fired
                self.lastfired = time.time()
                #adds the player to the list
                PlayerList.append(self)
        def SetPos(self, position):
                if not self.alive: return #doesn't continue if dead
                #moves the player
                self.position += position
                self.body1 += position
                self.body2 += position
                self.wep1 += position
                self.wep2 += position
                self.old += [self.body1, self.body2, self.wep1, self.wep2]
        def Reload(self, RenderPlayer):
                self.curwep = weapon.WeaponList[self.weapon] #updates current weapon
                if time.time() - self.lastfired > self.curwep.rof and self.reloading: #if still reloading
                        #makes the player no longer reloading
                        self.reloading = False
                        self.wep1col = self.curwep.wep1
                        self.wep2col = self.curwep.wep2
                        RenderPlayer(self) #renders new state
                elif not self.reloading and time.time() - self.lastfired < self.curwep.rof: #if not reloading
                        #makes the player start reloading
                        self.reloading = True
                        self.wep1col = config.Color8
                        self.wep2col = config.Color8
                        RenderPlayer(self) #renders new state
        def ChangeWep(self):
                #if not reloading, updates the player's weapon visual
                if not self.reloading:
                        self.curwep = weapon.WeaponList[self.weapon]
                        self.wep1col = self.curwep.wep1
                        self.wep2col = self.curwep.wep2
        def Shoot(self, PosCheck):
                #shoots the player's current weapon
                if time.time() - self.lastfired < self.curwep.rof: #checks if you can currently fire
                        return
                x = 0
                if self.direction == 1 or self.direction == 2: #sets the axis
                        x = 1
                        #makes a new projectile
                projectiles.Projectile(self.direction, PosCheck(self.position, self.direction)[x], self.curwep.ttl, self.curwep.speed, self.curwep.accuracy)
                #updates when last fired
                self.lastfired = time.time()
        #rotates the player to the new direction
        def Up(self):
                self.body1 = self.position + drop
                self.body2 = self.position + drop - 1
                self.wep1 = self.position
                self.wep2 = self.position - 1
                self.old = [self.body1, self.body2, self.wep1, self.wep2]
                self.direction = 0

        def Right(self):
                self.body1 = self.position + drop - 1
                self.body2 = self.position - 1
                self.wep1 = self.position + drop
                self.wep2 = self.position
                self.old = [self.body1, self.body2, self.wep1, self.wep2]
                self.direction = 1

        def Down(self):
                self.body1 = self.position - 1
                self.body2 = self.position
                self.wep1 = self.position + drop - 1
                self.wep2 = self.position + drop
                self.old = [self.body1, self.body2, self.wep1, self.wep2]
                self.direction = 1

        def Left(self):
                self.body1 = self.position
                self.body2 = self.position + drop
                self.wep1 = self.position - 1
                self.wep2 = self.position + drop - 1
                self.old = [self.body1, self.body2, self.wep1, self.wep2]
                self.direction = 1

def AddPlayers():
        #initially adds all the players
        Player1 = Player(50, 1)
        Player2 = Player(100, 2)
        Player3 = Player(150, 3)
        Player4 = Player(200, 4)
