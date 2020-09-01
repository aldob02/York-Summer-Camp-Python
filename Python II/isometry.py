import turtle
turtle.speed(0)

# Example:
# >>> drawBox(0, 0)
# >>> drawBox(100, 50)
def drawBox(x, y):
    
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

    turtle.color("red")
    turtle.begin_fill()
    turtle.setpos(x+87, y+50)
    turtle.setpos(x+87, y+150)
    turtle.setpos(x, y+100)
    turtle.setpos(x, y)
    turtle.end_fill()

    turtle.color("blue")
    turtle.begin_fill()
    turtle.setpos(x-87, y+50)
    turtle.setpos(x-87, y+150)
    turtle.setpos(x, y+100)
    turtle.setpos(x, y)
    turtle.end_fill()
    
    turtle.penup()
    turtle.setpos(x, y+100)
    turtle.pendown()
    
    turtle.color("green")
    turtle.begin_fill()
    turtle.setpos(x+87, y+150)
    turtle.setpos(x, y+200)
    turtle.setpos(x-87, y+150)
    turtle.setpos(x, y+100)
    turtle.end_fill()

# drawing boxes with 2D coordinates - delete ''' to uncomment
'''
drawBox(-87, 50)
drawBox(-174, 0)
drawBox(-261, -50)
drawBox(-348, -100)
drawBox(-261, -150)
drawBox(-174, -200)
drawBox(0, 0)
drawBox(87, -50)
drawBox(174, -100)
drawBox(87, -150)
drawBox(0, -200)
drawBox(-87, -250)
drawBox(174, 0)
drawBox(174, 100)
'''

# convert a 3D coordinate into a 2D location on the screen to draw the cube
# Example:
# >>> drawBox3D(0, 0, 0)
# >>> drawBox3D(0, 0, 1)
# >>> drawBox3D(0, 1, 0)
def drawBox3D(x, y, z):

    # Convert 3D point to 2D point
    x2D = 87*x - 87*y
    y2D = 100*z - 50*x - 50*y

    drawBox(x2D, y2D)

# drawing boxes with 3D coordinates
drawBox3D(0, 0, 0)
drawBox3D(1, 0, 0)
drawBox3D(0, 1, 0)
drawBox3D(0, 0, 1)
drawBox3D(3, 0, 1)
