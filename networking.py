import socket
import config
import pickle
import struct

###SVR###
SVs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
SVs.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

###CL###
CLs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
CLs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
CLs.bind(('', config.PORT))
group = socket.inet_aton(config.CAST)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
CLs.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

def SendArrSVR(server, port, array):
    s.connect((server,port))
    s.send(array.encode())
    result = s.recv(PACKET_SIZE)

def SendArrCL():
        SVs.sendto(pickle.dumps(config.MAP), (config.CAST,config.PORT))
"""s.connect((config.CAST,config.PORT))
s.send(pickle.dumps(config.MAP))
result = s.recv(4096)"""
def ReceiveCL():
        print("waiting")
        data,address = CLs.recvfrom(config.PACKET_SIZE)
        print("received " + str(len(pickle.loads(data))) + " from " + str(address))
        print(pickle.loads(data))
        return pickle.loads(data)
