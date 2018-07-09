import config
import menu
import display
import math
import game
import pickle
import networking
import time
import threading
import random
import player
import sys

started = False

Tick = time.time()

def GenerateMap():
        #randomly generates a map
        config.MAP = [] #this to not have a huge map in config, and to make it automatically get a size
        for x in range(int(config.PI_COUNT * config.SCREEN_SIZE * config.SCREEN_SIZE)): #based on various factors, creates the map array
                i = random.randint(1,config.MAP_CHANCE) #the random chance to spawn an obstacle
                if i == 1:
                        config.MAP.append(config.Color7) #spawns an obstacle
                else:
                        config.MAP.append(config.Color0) #spawns nothing
#runs initial functions
GenerateMap()
player.AddPlayers()
game.GameStart()
config.InitCol()
dumped = pickle.dumps(config.MAP)
print("Map Len " + str(len(config.MAP)))
config.DPS(sys.getsizeof(dumped)) #to figure out the packet size
time.sleep(1)

def Start():
        started = True
        for ply in player.PlayerList:
                game.RenderPlayer(ply)   

def Main():
        global started
        global Tick
        while True:
                if game.GameOver: #runs this if the game is over
                        #sets the map to display the winner's color
                        for x in range(len(config.MAP)): 
                                config.MAP[x] = game.GameWin
                        time.sleep(2) #delays
                        #updates display (looped to make sure all Pis get this)
                        for x in range(5):
                                display.UpdateDisplaySVR()
                        #delays, then resets by re-running initial functions
                        time.sleep(5)
                        print("Game Resetting")
                        GenerateMap()
                        player.PlayerList = []
                        player.AddPlayers()
                        config.InitCol()
                        game.GameStart()
                        started = False #makes this re-run some other initial functions
                        time.sleep(1) #delays to avoid issues
                if Tick + config.TickRate < time.time():
                        #keeps updating the game and the displays
                        game.runGame()
                        display.UpdateDisplaySVR()
                        if not started:
                                Start() #runs some startup stuff
                        Tick = time.time() #updates the ticker time

#creates some threads
thread = threading.Thread(target=networking.ReceiveSVR)
thread.start()
thread2 = threading.Thread(target=Main)
thread2.start()
