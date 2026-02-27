import turtle as t
import time

def triangle(recursionsamount,drawer):
    if recursionsamount == 0: return recursionsamount

    drawer.speed(0)

    trisize = 1000 * (.5**recursionsamount)

    drawer.teleport(-100, -100)

    for i in range(3):
        drawer.forward(trisize)
        drawer.left(120)
    
    drawer.forward(trisize*.5)
    drawer.left(120)
    drawer.forward(trisize*.5)
    drawer.right(120)
    drawer.forward(trisize*.5)
    drawer.right(120)
    drawer.forward(trisize*.5)
    drawer.right(60)
    drawer.forward(trisize*.5)
    drawer.right(180)
    
    """for i in range(3):
        drawer.right(120)
        drawer.forward(trisize)
    
    for i in range(3):
        drawer.right(60)
        drawer.forward(trisize)"""
        

    triangle(recursionsamount-1, drawer)

drawer = t.Turtle()
"""drawer.hideturtle()"""


triangle(5, drawer)

t.done()