import networking
import config
from sense_emu import SenseHat

DisplaySense = SenseHat()

def UpdateDisplaySVR():
        networking.SendArrCL() #sends updated map to client
def UpdateDisplayCL(map):
        SenseHat().set_pixels(map) #displays the map
def SendID(ID):
        DisplaySense.show_message(str(ID), config.TEXTSPEED) #shows the message
