# this file just draws the cube with dots on the vertices
# see isometry.py for the actual functions

import turtle
turtle.speed(0)

def drawBox(x, y):
    
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

    turtle.color("green")
    turtle.begin_fill()
    turtle.setpos(x+87, y+50)
    turtle.setpos(x+87, y+150)
    turtle.setpos(x, y+100)
    turtle.setpos(x, y)
    turtle.end_fill()

    turtle.color("grey")
    turtle.begin_fill()
    turtle.setpos(x-87, y+50)
    turtle.setpos(x-87, y+150)
    turtle.setpos(x, y+100)
    turtle.setpos(x, y)
    turtle.end_fill()
    
    turtle.penup()
    turtle.setpos(x, y+100)
    turtle.pendown()
    
    turtle.color("orange")
    turtle.begin_fill()
    turtle.setpos(x+87, y+150)
    turtle.setpos(x, y+200)
    turtle.setpos(x-87, y+150)
    turtle.setpos(x, y+100)
    turtle.end_fill()

drawBox(0, 0)

turtle.color("black")

turtle.penup()
turtle.setpos(0, 0)
turtle.dot()
turtle.penup()
turtle.setpos(87, 50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.setpos(87, 150)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.setpos(0, 200)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.setpos(-87, 150)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.setpos(-87, 50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.setpos(0, 100)
turtle.pendown()
turtle.dot()
    
turtle.penup()
turtle.setpos(99999, 99999)
