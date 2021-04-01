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
server = ("192.168.31.154", 11719)

# сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

name = input('$ name: ')
# отправка на сервер
name_1 = '[' + name + '] => join server'
s.sendto(name_1.encode("utf-8"), server)

done=False
join = False
rT = threading.Thread(target = receving, args = ("RecvThread", s, done))
rT.start()

# False == False -> True
while done==False: 
    try:
        message=input('message -> ')
        s.sendto(('['+name+'] => '+message).encode("utf-8"), server)
    except:
        name_2 =  '[' + name + '] <= left server'
        s.sendto(name_2.encode("utf-8"), server)
        done=True

rT.join()
s.close()
