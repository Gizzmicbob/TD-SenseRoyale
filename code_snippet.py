##old##
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import networking.py
import random
import time
import socket

sense = SenseHat()
ID = 0
tempID = 0
IDed = False
textSpeed = 0.04

unPressed = True

Checked = 0
Mode = "Client"

HOST = '224.0.0.1'
PORT = 27030

def disID():
    sense.show_message(str(tempID), textSpeed)
def disMode():
    sense.show_message(str(tempID), textSpeed)
        
def checkID():
    global ID
    global tempID
    global IDed
    global unPressed
    global Checked
    global Mode
    if Checked == 0:
        sense.show_message(str(tempID), textSpeed)
    elif Checked == 1:
        sense.show_message(Mode, textSpeed)
    for event in sense.stick.get_events():
        print(Checked)
        if event.action == "released":
            unPressed = True
            return
        if not unPressed:
            return
        unPressed = False
        if event.direction == "middle":
            if Checked == 0:
                ID = tempID
                IDed = True
                Checked = 1
            elif Checked == 1:
                Checked = 2
        elif event.direction == "right":
            if Checked == 0:
                tempID += 1
            else:
                Mode = "Client"
        elif event.direction == "left":
            if Checked == 0:
                tempID -= 1
            else:
                Mode = "Server"

def Server()
    
            
Players = "test"
temp = False
while True:
    if Checked < 2:
        checkID()
    else:
        print(Mode)
        if Mode == "Server":
            #if not temp:
            #    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            #        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
            #        s.sendto(Players.encode(), (HOST,PORT))
            #data, addr = socket.recvfrom(1024)
            Server()
            print(Mode)
        elif Mode == "Client":
            sense.show_message("a" + str(ID), textSpeed)


###networking stuff###

HOST_IP = "0.0.0.0" # all interfaces
SENDER_PORT = 1501
# 224.0.0.1 thru 224.255.255.255
# (ping 224.0.0.1 for the group mulitcast server list)
MCAST_ADDR = "224.0.0.1" 
MCAST_PORT = 1600
TTL=31# valid value are 1-255, <32 is local network

class producer:
    def init(self, sender_ip=HOST_IP, sender_port=SENDER_PORT, ttl=TTL):
        try:
            self.sock = socket.socket(socket.AF_INET,
                                      socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.sock.bind((sender_ip,sender_port))
            self.sock.setsockopt(socket.IPPROTO_IP,
                                 socket.IP_MULTICAST_TTL, ttl)
        except socket.error, e:
            if socket.error == 10048:
                self.init(sender_ip,sender_port+1,ttl)

    def send(self, msg="", mcast_addr=MCAST_ADDR, mcast_port=MCAST_PORT,):
        pickled_msg = pickle.dumps(msg)
        self.sock.sendto(pickled_msg, (mcast_addr, mcast_port))

    def host_name(self):
        return socket.gethostname()
class consumer:
    def init(self, client_ip=HOST_IP, mcast_addr=MCAST_ADDR,
                 mcast_port=MCAST_PORT, ttl=TTL, blocking=0):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind((client_ip, mcast_port))
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                             socket.inet_aton(mcast_addr) + socket.inet_aton(client_ip))
        self.sock.setblocking(blocking)

    def receive(self, size=1024):
        try:
            pickled_data, addr = self.sock.recvfrom(size)
            data = pickle.loads(pickled_data)
            return (addr,data)
        except socket.error, e:
            return None

    def host_name(self):
        return socket.gethostname()