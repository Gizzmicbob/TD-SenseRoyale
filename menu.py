from sense_emu import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import config
import display

MenuSense = SenseHat()
        
def ID_Choice():
    for event in MenuSense.stick.get_events():
        if event.action == "released":
            break
        elif event.direction == "middle":
            config.ID_Set = True
        elif event.direction == "right":
            config.ID += 1
        elif event.direction == "left":
            config.ID -= 1
    display.SendID()
