"""
Relógio feito com turle
"""

from turtle import *
import time

bgcolor('black')
color('white')

speed(8)

x=-30
hour = time.localtime(time.time()).tm_hour
minute = time.localtime(time.time()).tm_min

left(60)

# clock model
for num in range(12):
    up()
    forward(200)
    down()
    write(num+1, font=['', 18])
    backward(30)
    up()
    home()
    right(x)
    x+=30
    down()

# reset turtle pos
def reset():
    up()
    home()
    down()

    left(90)

width(3)

reset()

right((minute*6))
forward(120)

reset()

right((hour*30))
forward(60)

hideturtle()

mainloop()
