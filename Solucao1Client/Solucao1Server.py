#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket,pickle,random
host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
lista =[]
print "ESSE E O SERVIDOR"

while 1:
    client, address = s.accept()
    data = client.recv(size)
    
    if data:
        data = pickle.loads(data)
        P = int(data[0])
        g = int(data[1])
        A = int(data[2])

        
        #lista =([P,g,A])
        
        print "Valor de P : ", P
        print "Valor de g : ", g
        print "Valor de A : ", A

        b=(random.randint(0, 50))

        #B=(lista[2]^b) % lista[0]
        #B=(A^b) % P
        B=(g^b) % P
        B = str(B)
        print "Resultador de B:", B
        
        #P=int(P)
        KdB=(A^b) % P
        KdB = str(KdB)

        print "AQUI ESTA O KDB = " ,KdB


        client.send(B)
        
           
        
    client.close()