from turtle import *

speed(8)
shape("turtle")

sides = 8
length = 100
fillcolor('pink')
begin_fill()

angle = 360/sides
for count in range(sides):
    forward(length)
    right(angle)
end_fill()






input()