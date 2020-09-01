import math

deltaX = 0.00001

def f(x):
    return math.sin(math.floor(10*x))

def integrate(minX, maxX):
    total = 0
    width = maxX - minX
    x = minX
    while x < maxX:
        y = f(x)
        section_size = y * deltaX
        total = total + section_size
        x = x + deltaX
    return total
