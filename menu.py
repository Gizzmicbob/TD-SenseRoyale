from sense_emu import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import config
import display

MenuSense = SenseHat()

tID = 0
def ID_Choice():
    global tID
    #gets joystick presses and updates the display
    for event in MenuSense.stick.get_events():
        if event.action == "released":
            break
        elif event.direction == "middle":
            pID = tID
            tID = 0
            return pID, True
        elif event.direction == "right":
            tID += 1
        elif event.direction == "left":
            tID -= 1
    display.SendID(tID)
    return 0, False
