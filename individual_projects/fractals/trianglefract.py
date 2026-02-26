import turtle as t
import time

def triangle(recursionsamount,drawer):
    if recursionsamount == 0: return recursionsamount

    drawer.speed(0)

    trisize = 1000 * (.5**recursionsamount)

    drawer.teleport(-100, -100)

    for recursion in range(recursionsamount):
        for i in range(3):
            drawer.forward(trisize)
            drawer.left(120)

    triangle(recursionsamount-1, drawer)

drawer = t.Turtle()
drawer.hideturtle()


triangle(5, drawer)

t.done()