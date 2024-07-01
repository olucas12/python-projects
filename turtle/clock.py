"""
Relógio que mostra as horas atuais da máquina, feito com turtle
"""

from turtle import *
import time

# reset position of turtle
def resetPos():
    up()
    home()
    down()

# draw the frame and intern shadow of clock
def clockFrame():
    speed(0)

    color('lightgray')

    begin_fill()
    fillcolor('white')

    width(11)

    up()
    goto(0,-245)
    down()
    circle(245)
    resetPos()

    end_fill()
    color('yellow')

    width(10)

    up()
    goto(0,-250)
    down()
    circle(250)
    resetPos()

    width(2)

x=-30
hour = time.localtime(time.time()).tm_hour
minute = time.localtime(time.time()).tm_min

clockFrame()

left(60)
bgcolor('black')
color('black')

# draw numbers of clock
for num in range(12):
    up()
    forward(200)
    down()
    write(num+1, align='center', font=['Arial', 18])
    backward(30)
    up()
    home()
    right(x)
    x+=30
    down()

speed(2)

width(4)

resetPos()

left(90)
right((minute*6))
forward(120)

resetPos()

left(90)
right((hour*30))
forward(75)

hideturtle()

mainloop()
