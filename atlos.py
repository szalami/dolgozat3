# File: terkup.py
# Author: Faragó Csaba
# Copyright: 2022, Faragó Csaba
# Group: SZOFT I-1-E
# Date: 2022-11-19
# Github: https://github.com/szalami/dolgozat3.git
# Licenc: GNU GPL

import math
from turtle import clear
import os
clear = lambda: os.system('cls')
clear()

print("Faragó Csaba")
print("SZOFT I-1-E")
print("2022-11-19")

print()

a = int(input("Az a oldal hossza/cm/: "))
b = int(input("A b oldal hossza/cm/: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print("Az átló hossza: {:.4f}".format(c), "cm")