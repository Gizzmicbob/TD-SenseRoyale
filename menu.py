from sense_emu import SenseHat, ACTION_PRESSED, ACTION_RELEASED
from config import *

sense = SenseHat()
        
def ID_Choice():
    sense.show_message(str(config.ID), config.TEXTSPEED)
    for event in sense.stick.get_events():
        if event.action == "released":
            return
        if event.direction == "middle":
                config.ID_Set = True
        elif event.direction == "right":
                config.ID += 1
        elif event.direction == "left":
                config.ID -= 1
        sense.show_message(str(config.ID), config.TEXTSPEED)
    print(config.ID_Set)
