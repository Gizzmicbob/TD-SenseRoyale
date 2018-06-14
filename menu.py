from sense_emu import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import config
import display
        
def ID_Choice():
    for event in SenseHat().stick.get_events():
        if event.action == "released":
            break
        if event.direction == "middle":
                config.ID_Set = True
        elif event.direction == "right":
                config.ID += 1
        elif event.direction == "left":
                config.ID -= 1
    display.SendID()
    print(config.ID_Set)
