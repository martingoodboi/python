from turtle import forward, left, right, penup, pendown, exitonclick
from math import sqrt

for _ in range (4):
    forward (100)
    left (90)

left (45)

for _ in range (2):
    forward (100 * sqrt(2))
    left (135)
    forward (100)
    left (135)

right (135)

for _ in range (2):
    left (45)
    forward ((100 * sqrt(2)/2))
    left (45)

exitonclick ()