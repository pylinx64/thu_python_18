# -*- coding: utf-8 -*-

import socket 
import threading
import time

# собираем сообщения с сервера
def receving (name, sock, switch):
    while not switch:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print('\n' + data.decode('utf-8'))
                time.sleep(0.2)
        except:
            pass

# ваш порт и ip
host = socket.gethostbyname(socket.gethostname())
port = 0

# сервера порт и ip
server = ("192.168.31.210", 11719)

# сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

name = input('$ name: ')
s.sendto(name.encode("utf-8"), server)
