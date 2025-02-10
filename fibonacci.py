#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

numero = int(input("Quanti termini? "))

# n1 = 0
# n2 = 1

n1, n2 = 0, 1


count = 0

if numero <= 0:
   print("Prego inserire un intero")
elif numero == 1:
   print(n2)
else:
   print("Sequenza di Fibonacci:")
   while count < numero:
       print(n1)
       esimo = n1 + n2
       n1 = n2
       n2 = esimo
       count += 1
