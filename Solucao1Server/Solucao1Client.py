#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import os
from simplecrypt import encrypt, decrypt
import socket,pickle
#
host = 'localhost'
port = 50000
size = 1024
print "ESSE O O CLIENTE"
#
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
chaveB = []

#teste de P
from random import randint
P=(randint(60, 512))
#print P;

def factorise(P):
	x = math.ceil(math.sqrt(P))
	y = x**2 - P
	while not math.sqrt(y).is_integer():
		x += 1
		y = x**2 - P
	return x + math.sqrt(y), x - math.sqrt(y)

#print(factorise(6857.0))

#if ((2**(P-1)) % P):
#    print "Teste 1 Primo"
#else:
#    print "Nao e primo"
#if ((3**(P-1)) % P):
#    print "teste 2 Primo"
#else:
#    print "Nao e primo"
#if ((4**(P-1)) % P):
#    print "teste 3 Primo"
#else:
#    print "Nao e primo"
#if ((5**(P-1)) % P):
#    print "teste 4 Primo"
#else:
#    print "Nao e primo"
#if ((6**(P-1)) % P):
#    print "teste 5 Primo"
#else:
#    print "Nao e primo"

#TESTE DE g

from random import randint
g=(randint(60, P-1))
#print g;

def factorise(g):
	x = math.ceil(math.sqrt(g))
	y = x**2 - g
	while not math.sqrt(y).is_integer():
		x += 1
		y = x**2 - g
	return x + math.sqrt(y), x - math.sqrt(y)

#print(factorise(6857.0))

#if ((2**(g-1)) % g):
#    print "Teste 1 Primo"
#else:
#    print "Nao e primo"
#if ((3**(g-1)) % g):
#    print "teste 2 Primo"
#else:
#    print "Nao e primo"
#if ((4**(g-1)) % g):
#    print "teste 3 Primo"
#else:
#    print "Nao e primo"
#if ((5**(g-1)) % g):
#    print "teste 4 Primo"
#else:
#    print "Nao e primo"
#if ((6**(g-1)) % g):
#    print "teste 5 Primo"
#else:
#    print "Nao e primo"

#RESULTADOS TESTADOS P e g

#print "Resultados"
#print ""
print " O VALOR DE P e :", P;
#print P;
#print ""
print " O VALOR DE g e:", g;
#print g;

#HOST A
from random import randint
a=(randint(0, 50))
#print "HOST A"
#print "Valor de a:"
#print a;

A=(g^a) % P
print "O VALOR DE A e:" , A;
#print A;


#envido da mensagem
P = str(P)
g= str(g)
a = str(a)
A = str(A)

msg = ([P,g,A])
msg = pickle.dumps(msg)
s.send(msg)
data = s.recv(size)

a=int(a)
P=int(P)
B= int(data)
data = int(data)

KdA=(B^a) % P
KdA = str(KdA)
print "Aqui esta KdA = ",KdA


#mensagem1=raw_input("Digite a mensagem para enviar para B     :   ")
#mensagemR1=encrypt(KdA, mensagem1)
#print mensagemR1
#msg1 = ([mensagemR1])
#msg1 = pickle.dumps(msg1)

#s.send(msg1)



s.close()

#print 'Received:', data
