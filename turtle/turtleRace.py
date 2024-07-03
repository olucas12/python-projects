from turtle import *
import random
import os

colors = ['red', 'blue', 'purple', 'orange', 'pink', 'white', 'brown', 'yellow', 'green', 'gray']

bgcolor('black')

def createRunners():
    t1 = Turtle()
    t1 = t1.color(f'{colors[random.randint(0, 9)]}')

    t2 = Turtle()
    t2 = t2.color(f'{colors[random.randint(0, 9)]}')

    t3 = Turtle()
    t3 = t3.color(f'{colors[random.randint(0, 9)]}')

    t4 = Turtle()
    t4 = t4.color(f'{colors[random.randint(0, 9)]}')

    t5 = Turtle()
    t5 = t5.color(f'{colors[random.randint(0, 9)]}')

    t6 = Turtle()
    t6 = t6.color(f'{colors[random.randint(0, 9)]}')

    t7 = Turtle()
    t7 = t7.color(f'{colors[random.randint(0, 9)]}')

    t8 = Turtle()
    t8 = t8.color(f'{colors[random.randint(0, 9)]}')


def makeTrack():

    x = -400
    y = 0

    track = Turtle()
    track.speed(0)
    track.color('white')
    track.right(90)
    for n in range(9):
        track.up()
        track.goto(x, 400)
        x = track.xcor()+100
        track.down()
        track.forward(400)
        track.color('gray')
        track.write(f'  {y}', align='left', font=('arial', 18, 'bold'))
        track.color('white')
        y+=100
        track.forward(400)
    
    track.hideturtle()

makeTrack()

createRunners()

mainloop()