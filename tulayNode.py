import socket
import asyncio

l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
l3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
l4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

l1.bind(('',12000))
l2.bind(('',12000))
l3.bind(('',12000))
l4.bind(('',12000))

