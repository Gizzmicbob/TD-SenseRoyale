import networking
import config
from sense_emu import SenseHat

DisplaySense = SenseHat()

def UpdateDisplaySVR():
	networking.SendArrCL()
def UpdateDisplayCL(map):
	SenseHat().set_pixels(map)
def SendID():
	DisplaySense.show_message(str(config.ID), config.TEXTSPEED)
