"""
coração feito com turtle
"""

from turtle import *

bgcolor('black')
color('red')

speed(0)

fillcolor('red')
begin_fill()

up()
goto(100, -100)
down()
circle(140)
up()
goto(xcor()+75, ycor()+19)
right(135)
down()
forward(249)
end_fill()

begin_fill()
up()
home()
goto(-100, -100)
down()
circle(140)
up()
goto(xcor()-75, ycor()+19)
right(45)
down()
forward(249)
x = pos()
end_fill()

up()
goto(x)
down()

begin_fill()

for s in range(4):
    left(90)
    forward(280)

end_fill()

hideturtle()
mainloop()
