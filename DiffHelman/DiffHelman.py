#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name:        Exercicio
# Purpose:
#
# Author:      André Breviglieri
#
# Created:     09/04/2018
# Copyright:   (c) SENAI 2018
# Licence:     <Andre Breviglieri>
#-------------------------------------------------------------------------------
#Fonte : http://mathworld.wolfram.com/FermatsFactorizationMethod.html
#Fonte : https://github.com/przebieglykaziu/fermat-factor
#UPGRADE PIP
#python -m pip install --upgrade pip
#PATH C:\Python27
#INSTALL DEPENDENCIAS VCForPython27.msi
#-------------------------------------------------------------------------------


import math
import os
from simplecrypt import encrypt, decrypt

#teste de P
from random import randint
P=(randint(60, 2048))
print P;

def factorise(P):
	x = math.ceil(math.sqrt(P))
	y = x**2 - P
	while not math.sqrt(y).is_integer():
		x += 1
		y = x**2 - P
	return x + math.sqrt(y), x - math.sqrt(y)

#print(factorise(6857.0))

if ((2**(P-1)) % P):
    print "Teste 1 Primo"
else:
    print "Nao e primo"
if ((3**(P-1)) % P):
    print "teste 2 Primo"
else:
    print "Nao e primo"
if ((4**(P-1)) % P):
    print "teste 3 Primo"
else:
    print "Nao e primo"
if ((5**(P-1)) % P):
    print "teste 4 Primo"
else:
    print "Nao e primo"
if ((6**(P-1)) % P):
    print "teste 5 Primo"
else:
    print "Nao e primo"

#TESTE DE g

from random import randint
g=(randint(60, P-1))
print g;

def factorise(g):
	x = math.ceil(math.sqrt(g))
	y = x**2 - g
	while not math.sqrt(y).is_integer():
		x += 1
		y = x**2 - g
	return x + math.sqrt(y), x - math.sqrt(y)

#print(factorise(6857.0))

if ((2**(g-1)) % g):
    print "Teste 1 Primo"
else:
    print "Nao e primo"
if ((3**(g-1)) % g):
    print "teste 2 Primo"
else:
    print "Nao e primo"
if ((4**(g-1)) % g):
    print "teste 3 Primo"
else:
    print "Nao e primo"
if ((5**(g-1)) % g):
    print "teste 4 Primo"
else:
    print "Nao e primo"
if ((6**(g-1)) % g):
    print "teste 5 Primo"
else:
    print "Nao e primo"

#RESULTADOS TESTADOS P e g

print "Resultados"
print ""
print " O VALOR DE P e :"
print P;
print ""
print " O VALOR DE g e:"
print g;

#RANDON "a" e "b"
#HOST A
from random import randint
a=(randint(0, 50))
print "HOST A"
print "Valor de a:"
print a;
#RANDON "a" e "b"
#HOST B
from random import randint
b=(randint(0, 50))
print "HOST B"
print "Valor de b :"
print b;

#HOST A
A=(g^a) % P
print "Resultador de A:"
print A;

#HOST B
B=(g^b) % P
print "Resultador de B:"
print B;

#CALCULO DE CHAVE K
# EM A
KdA=(B^a) % P
print "Resultador de KdA:"
print KdA;
#CALCULO DE CHAVE K
# EM B
KdB=(A^b) % P
print "Resultador de KdB:"
print KdB;

KdA = str(KdA)
KdB = str(KdB)

#TESTE DE MENSAGEM CRIPTOGRAFADA A
mensagem1=raw_input("Digite a mensagem para enviar para B     :   ")
mensagemR1=encrypt(KdA, mensagem1)

print "******"
print " MENSAGEM CRIPTOGRAFADA"
print "******"
print ""
print mensagemR1;
print ""
print "******"

#TESTE DE MENSAGEM CRIPTOGRAFADA B
mensagem2=raw_input("Digite a mensagem para enviar para A    :    ")
mensagemR2=encrypt(KdA, mensagem2)
#print mensagemR2;
print "******"
print " MENSAGEM CRIPTOGRAFADA"
print "******"
print ""
print mensagemR2;
print ""
print "******"

os.system ("cls")

print "******"
print "DECRIPTOGRAFANDO AS MENSAGENS"
print "******"
print ""
#TESTE DE MENSAGEM DECRIPTOGRADA DE A
mensagemR1=decrypt(KdB, mensagemR1)
print ""
print "******"
print " MENSAGEM DECRIPTOGRADA KdA"
print "******"
print ""
print mensagemR1;
print ""
print "******"
print ""
mensagemR2=decrypt(KdA, mensagemR2)
#print mensagemR2;
print ""
print "******"
print " MENSAGEM DECRIPTOGRADA DE B"
print "******"
print ""
print mensagemR2;
print ""
print "******"

print "******"
print "FIM DA COMUNICACOA"
print "******"
