import networking.py
import config.py
from sense_hat import SenseHat
sense = SenseHat()

def UpdateDisplaySVR():
	SendArrCL(HOST,PORT,MAP)
def UpdateDisplayCL(map):
	sense.set_pixels(map)