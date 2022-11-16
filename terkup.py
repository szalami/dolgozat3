# Faragó Csaba
# SZOFT I-1-E
# 2022-11-17
# 
import math
from turtle import clear
import os
clear = lambda: os.system('cls')
clear()

print("Faragó Csaba")
print("SZOFT I-1-E")
print("2022-11-17")

print()

r = int(input("Az alap sugara: "))
h = int(input("A kúp magassága: "))

v = (1/3) * pow(r, 2) * math.pi * h

print("A kúp térfogata: ", v)
print()

