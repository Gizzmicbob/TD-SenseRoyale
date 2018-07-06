#import funcs
PlayerList = []
drop = 16
def Up(ply):
        ply.body1 = ply.position + drop
        ply.body2 = ply.position + drop - 1
        ply.wep1 = ply.position
        ply.wep2 = ply.position - 1
        ply.old = [ply.body1, ply.body2, ply.wep1, ply.wep2]
        ply.direction = 0

def Right(ply):
        ply.body1 = ply.position + drop - 1
        ply.body2 = ply.position - 1
        ply.wep1 = ply.position + drop
        ply.wep2 = ply.position
        ply.old = [ply.body1, ply.body2, ply.wep1, ply.wep2]
        ply.direction = 1

def Down(ply):
        ply.body1 = ply.position - 1
        ply.body2 = ply.position
        ply.wep1 = ply.position + drop - 1
        ply.wep2 = ply.position + drop
        ply.old = [ply.body1, ply.body2, ply.wep1, ply.wep2]
        ply.direction = 1

def Left(ply):
        ply.body1 = ply.position
        ply.body2 = ply.position + drop
        ply.wep1 = ply.position - 1
        ply.wep2 = ply.position + drop - 1
        ply.old = [ply.body1, ply.body2, ply.wep1, ply.wep2]
        ply.direction = 1
        

class Player:
        ###important - integrate with funcs###
        def __init__(self, position, ID):
                self.position = position
                self.body1 = position
                self.body2 = position - 1
                self.wep1 = position + drop
                self.wep2 = position + drop - 1
                self.old = [self.body1, self.body2, self.wep1, self.wep2]
                self.weapon = 0
                self.alive = True
                self.id = ID
                self.direction = 0
                PlayerList.append(self)
        def SetPos(self, position):
                if not self.alive: return
                self.position += position
                self.body1 += position
                self.body2 += position
                self.wep1 += position
                self.wep2 += position
                self.old += [self.body1, self.body2, self.wep1, self.wep2]
                

Player1 = Player(66, 1)
Player2 = Player(100, 2)
Player3 = Player(200, 3)
Player4 = Player(300, 4)
