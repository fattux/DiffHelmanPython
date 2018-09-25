#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "SERVER"
import socket, pickle
import sys
import codecs
import random
from Crypto.Cipher import AES
from time import sleep
from simplecrypt import encrypt, decrypt
import os

# Gerar o valor de "b" aleatoriamente

taman_chave = 16-1
chaveb = random.randrange (2**taman_chave)
b = random.randrange(1, chaveb)
print 'Valor de "b" = ', b

###############################################################
# Recebe os Valores de "P", "G" e "A"
server = ('127.0.0.1',50000)
size = 2048
backlog = 5
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind (server)
sock.listen (backlog)
connection, client = sock.accept()
print >>sys.stderr, 'Conectado', client
while 1:
	#print >>sys.stderr, 'Aguardando Conexão'
	#try:
	#print 'Aguardando recebimento dos valores P,G e A '
	data = connection.recv(size)
	if not data: break
	data = pickle.loads(data)
	P = int(data[0])
	G = int(data[1])
	A = int(data[2])
	connection.close
###############################################################
print "P = ", P
print "G = ", G
print "A = ", A

#####################
B = 0
B = ((G**b) % P)
#####################

sleep (2)

print 'Valor de B - ', B
B = str(B)
###############################################################
# envia o valor de B para cliente A
sleep (2)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 40000)
sock.connect(server_address)
msgb = ([B,])
msgb = pickle.dumps(msgb)
sock.send(msgb)
###############################################################

Kb = 0
Kb = ((A**b)% P)

print 'Kb = ', Kb
Kb = str(Kb)
print ("")
print ("Valor de Kb string - ", Kb)
print ("")
###############################################################
# Recebe a Mensagem Encriptada para Descriptografar"
server = ('127.0.0.1',30000)
size = 2048
backlog = 5
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind (server)
sock.listen (backlog)
sock, client = sock.accept()
print >>sys.stderr, 'Conectado', client
dados = sock.recv(size)
print "Mensagem Cryptografada :: >>> " ,dados
sleep (5)
mensagema = decrypt(Kb,dados)
mensagem = ' Mensagem Recebida...'
connection.send(mensagem)
print "Mensagem recebida : > ",mensagema
#if not dados: break
sock.send('Mensagem Recebida...!')
sock.close
###############################################################
##print data
#p#rint ' '
#print Kb
#sleep (5)
#mensagema = decrypt(Kb, dados) 
#sleep (3)
#print ' ' 
#print mensagema
#sleep (2)
