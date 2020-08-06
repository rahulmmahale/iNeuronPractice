##3. Write a Python program to find the volume of a sphere with diameter 12 cm.
## Formula: V=4/3 * π * r 3

import math

r = 12 /2

V = 4/3 * math.pi * math.pow(r,3)

print ("Volume: "+ str(V) )