import config

WeaponList = [] #the list of weapons
class Weapon:
        ###important - integrate with funcs###
        def __init__(self, ttl, speed, rof, accuracy, wep1, wep2):
                self.ttl = ttl #bullet time to live
                self.speed = speed #bullet speed
                self.rof = rof #rate of fire
                self.accuracy = accuracy #how accurate the weapon is
                #weapon colors
                self.wep1 = wep1
                self.wep2 = wep2
                WeaponList.append(self) #adds weapon to the list

#initiates weapons
wep1 = Weapon(16, 0.2, 0.5, 75, config.Color5, config.Color8)
wep2 = Weapon(128, 0.01, 2.5, 100, config.Color5, config.Color5)
wep3 = Weapon(2, 0.01, 0, 0, config.Color8, config.Color8)
