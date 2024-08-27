from turtle import *
import random
import os
import time

Screen().setup(width=1100, height=600)
Screen().title('Turtle Race 1.0 - Python')

turtles = []
colors = ['red', 'blue', 'purple', 'brown', 'green', 'white', 'yellow', 'green']
step = 4

bgcolor('black')

def Winner(t, color):
    Screen().clear()
    bgcolor(color)
    bgcolor('black')
    win = Turtle()
    win.hideturtle()
    win.speed(0)
    win.up()
    win.goto(0, 0)
    win.down()
    win.color(color)
    win.write(f'  {t.color()[0].capitalize()} wins!', align='center', font=('inter', 18, 'bold'))


def startRun():
    winner = False
    while winner != True:
        for t in turtles:
            t.forward(random.randint(step, step+4))
            if (t.xcor() < 450):
                pass
            else:
                winner = True
                time.sleep(2)
                Winner(t, t.color()[1])
                break

def createRunners():
    i=0
    for turtle in range(8):
        t = Turtle()
        t.color(colors[i])
        turtles.append(t)
        i+=1

def initRunners():
    createRunners()
    y=0
    for t in turtles:
       t.speed(0)
       t.up() 
       t.goto(-450, -250+y)
       y+=85
       t.down()
       t.shape('turtle')

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
        track.color('#303030')
        track.write(f'  {y}', align='left', font=('arial', 18, 'bold'))
        track.color('white')
        y+=100
        track.forward(400)

makeTrack()

initRunners()

startRun()

mainloop()