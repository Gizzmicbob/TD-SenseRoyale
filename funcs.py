import config
import math

def DropLine():
        #drops a line down
        return int(math.sqrt(config.PI_COUNT) * config.SCREEN_SIZE)
def DropSect():
        #drops a section down
        return math.sqrt(config.PI_COUNT) * config.SCREEN_SIZE * config.SCREEN_SIZE
