import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def SendArrSVR(server, port, array):
	s.connect((server,port))
	s.send(array.encode())
	result = s.recv(4096)

def SendArrCL(cast, port, array):
	s.connect((cast,port))
	s.send(array.encode())
	result = s.recv(4096)
