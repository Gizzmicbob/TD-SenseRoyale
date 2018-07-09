import socket
import config
import pickle
import struct
import game
import funcs

###Server Out Sockets###
SVs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
SVs.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
#Server in Socket
SVu = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#tries to bind the socket, else not server
try:
    SVu.bind((config.HOST,config.PORT2))
except OSError:
    print("Not Server")
###Client In Sockets###
CLs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
CLs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
CLs.bind(('', config.PORT))
group = socket.inet_aton(config.CAST)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
CLs.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
#Client out socket
CLu = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def SendSVR(key, ID):
    #send the keypresses to the server
    array = [key, ID]
    CLu.sendto(pickle.dumps(array), (config.HOST,config.PORT2))

def SendArrCL():
    #sends the map to the clients
        SVs.sendto(pickle.dumps(config.MAP), (config.CAST,config.PORT))
def ReceiveCL():
        #recieves the map from the server
        data,address = CLs.recvfrom(config.PACKET_SIZE)
        funcs.Dropper()
        return pickle.loads(data)
def ReceiveSVR():
    while True:
        #receives keys from the client
        data,address = SVu.recvfrom(config.PACKET_SIZE)
        game.ReceiveKey(pickle.loads(data))

