import networking.py
import config.py
from sense_hat import SenseHat

def UpdateDisplaySVR():
	SendArrCL(HOST,PORT,MAP)
def UpdateDisplayCL(map):
	SenseHat().set_pixels(map)
def SendID():
	SenseHat().show_message(str(config.ID), config.TEXTSPEED)