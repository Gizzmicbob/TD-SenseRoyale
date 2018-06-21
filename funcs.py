import config
import math
import display

def DropLine():
        #drops a line down
        return int(math.sqrt(config.PI_COUNT) * config.SCREEN_SIZE)
def DropSect():
        #drops a section down
        return math.sqrt(config.PI_COUNT) * config.SCREEN_SIZE * config.SCREEN_SIZE
def Dropper():
    #subtract 1 to match array index at 0?
    sideLen = math.sqrt(config.PI_COUNT) * config.SCREEN_SIZE #length of a side of the whole display
    pPlace = config.ID * config.SCREEN_SIZE - config.SCREEN_SIZE #start position - remember, array starts at 0
    drops = pPlace // sideLen
    dropAmount = max(drops * config.SCREEN_SIZE * sideLen, 0) #how much to drop, -1 zero it for array
    remainder = pPlace % sideLen #position after drop
    fPos = dropAmount + remainder #final position
    miniMap = []
    fPos = int(fPos)
    remainder = int(remainder)
    sideLen = int(sideLen)
    x = fPos
    iters = 1
    sPos = fPos
    while x < fPos + (sideLen * config.SCREEN_SIZE): #probs not right
        miniMap.append(config.MAP[int(x)])
        if x == sPos + config.SCREEN_SIZE or (iters == 1 and x == sPos + config.SCREEN_SIZE - 1): #be sure 0 works
            x += DropLine() - config.SCREEN_SIZE #+/-
            sPos = x
            iters += 1
        if len(miniMap) == 64:
            break
        x += 1
    display.UpdateDisplayCL(miniMap)
    miniMap = []
