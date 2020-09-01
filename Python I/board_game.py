import turtle
turtle.speed = 0
turtle.tracer(0, 0)
curr_x = 50
curr_y = 40
points = 0

def draw_character(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setpos(x-25, y)
    turtle.setpos(x, y+25)
    turtle.setpos(x+25, y)
    turtle.setpos(x-15, y)
    turtle.setpos(x-15, y-15)
    turtle.setpos(x+15, y-15)
    turtle.setpos(x+15, y)
    turtle.setpos(x-7, y)
    turtle.setpos(x-7, y-5)
    turtle.setpos(x-5, y-5)
    turtle.setpos(x-5, y)
    turtle.setpos(x+7, y)
    turtle.setpos(x+7, y-5)
    turtle.setpos(x+5, y-5)
    turtle.setpos(x+5, y)
    turtle.update()

def delete_character(x, y):
    turtle.penup()
    turtle.setpos(x-25, y-15)
    turtle.color('white', 'white')
    turtle.begin_fill()
    turtle.pendown()
    turtle.setpos(x-25, y+25)
    turtle.setpos(x+25, y+25)
    turtle.setpos(x+25, y-15)
    turtle.setpos(x-25, y-15)
    turtle.end_fill()
    turtle.color('black', 'black')
    turtle.update()

def draw_board():
    max_width = turtle.window_width()/2
    max_height = turtle.window_height()/2
    width = -max_width
    for i in range(10):
        width = width + max_width/5
        turtle.penup()
        turtle.setpos(width, max_height)
        turtle.pendown()
        turtle.setpos(width, -max_height)
    height = -max_height
    for i in range(10):
        height = height + max_height/5
        turtle.penup()
        turtle.setpos(-max_width, height)
        turtle.pendown()
        turtle.setpos(max_width, height)
    turtle.update()

def right():
    global curr_x, curr_y
    max_width = turtle.window_width()/2
    delete_character(curr_x, curr_y)
    curr_x = curr_x + max_width/5
    draw_character(curr_x, curr_y)
    turtle.update()
    new_space()

def left():
    global curr_x, curr_y
    max_width = turtle.window_width()/2
    delete_character(curr_x, curr_y)
    curr_x = curr_x - max_width/5
    draw_character(curr_x, curr_y)
    turtle.update()
    new_space()

def up():
    global curr_x, curr_y
    max_height = turtle.window_height()/2
    delete_character(curr_x, curr_y)
    curr_y = curr_y + max_height/5
    draw_character(curr_x, curr_y)
    turtle.update()
    new_space()

def down():
    global curr_x, curr_y
    max_height = turtle.window_height()/2
    delete_character(curr_x, curr_y)
    curr_y = curr_y - max_height/5
    draw_character(curr_x, curr_y)
    turtle.update()
    new_space()

def new_space():
    global curr_x, curr_y, points
    if (curr_x, curr_y) == (146, 40):
        print('You gain 1 point!')
        points = points + 1
    if (curr_x, curr_y) == (146, 121):
        print('You lose 1 point!')
        points = points - 1
    print('You have ' + str(points) + ' points.')