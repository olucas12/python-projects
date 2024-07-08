from turtle import *
import random
import os

Screen().setup(width=1100, height=600)

turtles = []
colors = ['red', 'blue', 'purple', 'brown', 'green', 'white', 'yellow', 'green']

bgcolor('black')

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
    
    track.hideturtle()

makeTrack()

initRunners()

mainloop()