import socket

myDomain = "fullerton.dchin.net"

myIP = socket.getaddrinfo(myDomain,0)[0][4][0]
print(myIP)
