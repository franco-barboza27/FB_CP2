import turtle
import random
from math import * 

# TREE GEN function

    # if the amount of recursions is = to the amount of possible combinations,
        # call the drawer with the big list
    


    # Keep looping
        # choose a number 1 in 2
        # add the number to a list

        # if the list is distinct in the big list,
            # call the function with recursions + 1

def tree_gen(depth, recursions, pen, branches):
    recurse = 2**depth#factorial(2+depth-1)//(factorial(depth-1) * factorial(2))
    if recursions == recurse:
        draw_tree(pen, 100, branches, recurse)
        pen.teleport(0, 0)
        pen.hideturtle()
        return None
    
    branch = []

    for i in range(depth):
        num = random.randint(1, 2)
        branch.append(num)

    if branch in branches:
        tree_gen(depth, recursions, pen, branches)
    else:
        branches.append(branch)
        tree_gen(depth, recursions+1, pen, branches)

# TREE DRAW function
    # if recursions == 0:
        # return Nothing

    # keep count of what number item it is
    # for every item in the list(list is collected based on the recursion amount)
        # go forward size^.5

        # if the item is 1,
            # turn like, 60 degrees right
        # otherwise:
            # turn like 60 degrees left
    
    # call TREE DRAW with recursion value -1

        
def draw_tree(pen, size, branches, recursions):
    if recursions == 0:
        return None
    
    pen.setheading(90)
    pen.teleport(0, 0)
    
    count = 0

    for path in branches[recursions-1]:
        pen.forward(size*.75**count)
        if path == 1:
            pen.left(30)
        else:
            pen.right(30)
        count += 1
    
    draw_tree(pen, size, branches, recursions-1)