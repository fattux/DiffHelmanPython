#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "CLIENTE"
import socket,pickle
import sys
import codecs
from Crypto.Cipher import AES
from time import sleep
import random
from simplecrypt import encrypt, decrypt

IPsvr1 = ''
IPsvr2 = ''

# Gerar os valores para "a" e "b" aleatoriamente

taman_chave = 16-1
chavea = (2**taman_chave)
a = random.randrange(1, chavea)
#chaveb = (2**taman_chave)
#b = random.randrange(1,chaveb)

print ' '
print 'Valor a = ', a
print ' '
#print 'Valor b = ', b
#print ' '

# Aqui vamos calcular o VALOR de P

numero = 0
while numero == 0 :
	P = random.randrange(32,256)
	if ((2**(P-1) % P == 1)) and ((3**(P-1) % P == 1)) and ((4**(P-1) % P == 1)) and ((5**(P-1) % P == 1)) and ((6**(P-1) % P == 1)):
		numero = 1
print 'Valor de P = ', P

# Aqui vamos calcular o VALOR de G

numero = 0
while numero == 0 :
	G = random.randrange(32,256)
	if ((2**(G-1) % G == 1)) and ((3**(G-1) % G == 1)) and ((4**(G-1) % G == 1)) and ((5**(G-1) % G == 1)) and ((6**(G-1) % G == 1)):
		numero = 1
print 'Valor de G = ', G

#Calcular A e B

A = 0
A = ((G**a) % P)

print 'Valor de A = ', A

##################################################################################
# Enviar os valores de "P", "G" e "A"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 50000)
sock.connect(server_address)
P = str(P)
G = str(G)
A = str(A)
msg = ([P,G,A])
msg = pickle.dumps(msg)
sock.send(msg)
##################################################################################

##################################################################################
# Recebe o valor de B
server = ('127.0.0.1',40000)
size = 2048
backlog = 5
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server)
sock.listen(backlog)
connection, client = sock.accept()
print >>sys.stderr, 'Conectado - ', client
while 1:
	data = connection.recv(size)
	if not data: break
	data = pickle.loads(data)
	B = int(data[0])
	connection.close
print ("")
print "Valor de B - ", B
##################################################################################		
P = int (P)

Ka = 0
Ka = ((B**a)% P)

print 'Ka = ', Ka
##################################################################################
# agora que calculamos as chaves podemos digitar a mensagem e criptografar

print ' Digite a mensagem para enviar ao Cliente B = '
mensagem = raw_input("")
Ka = str(Ka)
print ("")
print ("Valor de Ka string - ", Ka)
print ("")
print 'Encriptando a Mensagem...'
print ' '
msgenvia = encrypt(Ka, mensagem)
sleep (3)
print 'Mensagem Criptografada = ', msgenvia
sleep (3)
print "Descriptar para Teste "
teste = decrypt (Ka, msgenvia)
print "Decriptada novamente para teste - ", teste
sleep (3)
##################################################################################
# Enviar Mensagem para B
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 30000)
sock.connect(server_address)
sock.send(msgenvia)
sleep (2)
print("Mensagem Enviada...")
resp = sock.recv(1024)
print 'Resposta de B - ', resp
sleep (2)
##################################################################################








