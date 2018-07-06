import config
import funcs
import game
drop = funcs.DropLine()
allProj = []
def IsEdge(pos):
        if pos in game.right or pos in game.left or pos in game.top or pos in game.bottom:
                return True
def CheckImp(proj, position, direction): #use other funcs later
        change = 0
        if direction == 0:
                change -= 16
        elif direction == 1:
                change += 1
        elif direction == 2:
                change += 16
        elif direction == 3:
                change -= 1
        if config.MAP[position + change] != config.Color0 or IsEdge(position + change):
                proj.toDie = True
class Projectile:
        ###important - integrate with funcs###
        def __init__(self, direction, position, ttl, speed):
                print("new proj" + str(position))
                self.direction = direction
                self.position = position
                self.old = position
                self.ttl = ttl
                self.speed = speed
                self.slow = True
                self.toDie = False
                self.buffer = True
                allProj.append(self)
        def Move(self):
                if self.speed == 0 or self.slow == True:
                        if self.toDie or self.ttl == 0:
                                config.MAP[self.position] = config.Color0
                                print("bullet lost")
                                allProj.remove(self)
                                return
                        CheckImp(self, self.position, self.direction)
                        self.ttl -= 1
                        self.slow = False
                        if self.direction == 0:
                                self.position -= 16
                        elif self.direction == 1:
                                self.position += 1
                        elif self.direction == 2:
                                self.position += 16
                        elif self.direction == 3:
                                self.position -= 1
                        if not self.buffer:
                                config.MAP[self.old] = config.Color0
                        else:
                                self.buffer = False
                        config.MAP[self.position] = config.Color6
                        self.old = self.position
                else:
                        self.slow = True
                
