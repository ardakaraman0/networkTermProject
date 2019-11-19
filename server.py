import random
from socket import *

server = socket(AF_INET, SOCK_DGRAM)

server.bind(('',12000))

while True:
    rand = random.randint(0,10)
    message, address = socket.recvfrom(1024)

    message = message.upper()

    if rand >= 4:
        server.sendto(message, address)
