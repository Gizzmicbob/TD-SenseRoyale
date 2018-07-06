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

Tick = time.time()

config.MAP = [] #this to not have a huge map in config, and to make it automatically get a size
for x in range(int(config.PI_COUNT * config.SCREEN_SIZE * config.SCREEN_SIZE)):
        i = random.randint(0,5)
        if i == 1:
                config.MAP.append(config.Color7)
        else:
                config.MAP.append(config.Color0)

def Main():
        global Tick
        while True:
                if Tick + config.TickRate < time.time():
                        game.runGame()
                        display.UpdateDisplaySVR()
                        Tick = time.time()

thread = threading.Thread(target=networking.ReceiveSVR)
thread.start()
thread2 = threading.Thread(target=Main)
thread2.start()
