import turtle
import math
turtle.speed(0)

# create and draw Box objects with:
# >>> box1 = Box(0, 0, 0)
# >>> box2 = Box(0, 0, 1)
# >>> box3 = Box(1, 1, 0)
# >>> box1.draw()
# >>> box2.draw()
# >>> box3.draw()
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "Box at (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    
    def get2DCoords(self):
        x2D = 87*self.x - 87*self.y
        y2D = 100*self.z - 50*self.x - 50*self.y
        return (x2D, y2D)
    
    def draw(self):
        (x, y) = self.get2DCoords()
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

lst = []
for i in range(6):
    lst.append(Box(0, i, 2*i))
    print(lst[i])

for box in lst:
    box.draw()