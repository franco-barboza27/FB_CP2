import turtle as t

# Draw ONE triangle
def triangle_draw(drawer, size):
    drawer.setheading(180)
    count = 0
    while count < 3:
        drawer.right(120)
        drawer.forward(size)
        count += 1

# this is the pattern for drawing triangles
# If the amount of recursions is ZERO draw a triangle
# on the FIRST run, draw a triangle
# go to the TOP of the triangle (to draw the next triforce.)
    # the distance is always = to 2^depth-1 BTW

def sierpinski_pattern(recursions, size, drawer):
    if recursions == 0:
        triangle_draw(drawer, size)
    else:
        sierpinski_pattern(recursions-1, size, drawer)
        drawer.right(120)
        drawer.forward(size * 2**(recursions-1))
        sierpinski_pattern(recursions-1, size, drawer)
        drawer.left(120)
        drawer.forward(size * 2**(recursions-1))
        sierpinski_pattern(recursions-1, size, drawer)
        drawer.forward(size * 2**(recursions-1))