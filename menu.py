from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import config.py

sense = SenseHat()
        
def ID_Choice():
    global ID
    for event in sense.stick.get_events():
        if event.action == "released":
            return
        if event.direction == "middle":
                ID_Set = True
        elif event.direction == "right":
                ID += 1
        elif event.direction == "left":
                ID -= 1
        sense.show_message(str(ID), TextSpeed)