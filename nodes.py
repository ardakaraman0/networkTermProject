import socket
import asyncio
import time
import netifaces

r1s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r1r2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r1d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r2s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r2d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r2r3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r3s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r3d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r1s.bind(('',12000))
r1r2.bind(('',12000))
r1d.bind(('',12000))
r2s.bind(('',12000))

r2d.bind(('',12000))
r2r3.bind(('',12000))
r3s.bind(('',12000))
r3d.bind(('',12000))


msg = 'sa'
returnmsg = 'as'
array = []

async def send(data, addr, port, Socket):
    await Socket.sendto(data, (addr, port))
    sentTime = time.clock()
    return sentTime

async def rec(socket, sentTime):
    data, addr = socket.recvfrom(2)
    recTime = time.clock()
    array.append(recTime - sentTime)


def finished(array):
    txtFile = open('txtFile.txt', 'w')
    txtFile.writelines(array)

def set_timer( time ):
    self.timer = Timer( 10.0, timeout )
    self.timer.start()

def main():
    time.sleep(20)
    
    while 1:
        


    return


