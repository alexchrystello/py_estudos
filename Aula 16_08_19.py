# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:42:01 2019

@author: alex
"""
#Tipo Inteiro (integer)
a = 56
b = 56
c = 363749028972666489276256898
type (a)
type (b)
type (c)

#Tipo Ponto Flutuante (Float)
a = 2.734
b = 4.6e9
c = .0065E-64
type (a)
type (b)
type (c)

a = 5 > 3
a

a = bool (3)
b = bool (0)
c = bool (-3)
d = bool (None)
e = bool ([ ]) # uma lista vazia (vamos ainda definir o que é uma lista)
f = bool ([3, 5, 'hi'])

#Tipo Boolean
a = [2,7,5,16]
b = 2
c = b in a
print (c)

# Listas e Tuplas Lists e Tuples
L = [4.5, -7.8, 'pickle', True, None, 5] # Lista
T = (4.5, -7.8, 'pickle', True, None, 5) # Tupla
Lista_dentro_Lista = [L, T]

print (Lista_dentro_Lista[0])