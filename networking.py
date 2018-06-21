import socket
import config
import pickle
import struct
import game

###SVR###
SVs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
SVs.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
#
SVu = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    SVu.bind((config.HOST,config.PORT2))
except OSError:
    print("Not Server")
###CL###
CLs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
CLs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
CLs.bind(('', config.PORT))
group = socket.inet_aton(config.CAST)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
CLs.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
#
CLu = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def SendSVR(key, ID):
    array = [key, ID]
    CLu.sendto(pickle.dumps(array), (config.HOST,config.PORT2))

def SendArrCL():
        SVs.sendto(pickle.dumps(config.MAP), (config.CAST,config.PORT))
        print("send")
def ReceiveCL():
        data,address = CLs.recvfrom(config.PACKET_SIZE)
        return pickle.loads(data)
def ReceiveSVR():
    while True:
        data,address = SVu.recvfrom(config.PACKET_SIZE)
        game.ReceiveKey(pickle.loads(data))

