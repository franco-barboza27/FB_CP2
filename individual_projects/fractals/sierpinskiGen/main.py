import individual_projects.fractals.sierpinskiGen.triangleFract as triangleFract, individual_projects.fractals.sierpinskiGen.helpers as helpers
import turtle

# ask for the kind of pattern (tree or triangle)
# ask for the amount of depth in the pattern (bigger = more repeats)

# call the tree file or the triangle file functions depending on which they do
def main():
    print("Would you like to:\n1. Triangle Fractal\n2. Fractal Tree (Doesn't work yet actually)")

    fractal = helpers.inputchecker(1)

    while True:
        depth = input("How many layers do you want to be (anymore than 6 takes a ton of time to finish)")

        try:
            depth = int(depth)
            break
        except:
            print("That wasn't a number!")
            continue

    # check what the depth for their pattern will be and make sure it works

    pen = helpers.turtlesetup()

    match fractal:
        case 1:
            triangleFract.sierpinski_pattern(depth, 500*.5**depth, pen)
    # go to the according pattern with an appropriate size

print("Hello, this is a fractal generator!")
print("It can generate a sierpinski triangle, and eventually a fractal tree (lets hope :)")

main()

turtle.done()