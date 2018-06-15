import config
import menu
import display
import math
import game
import pickle

config.MAP = [] #this to not have a huge map in config, and to make it automatically get a size
for x in range(int(config.PI_COUNT * config.SCREEN_SIZE)):
        config.MAP.append(config.Color0)

while True:
        game.runGame()
        display.UpdateDisplaySVR()
