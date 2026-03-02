import turtle as t

# sets up the turtle color
def turtlesetup():
    screen = t.Screen()
    drawer = t.Turtle()
    drawer.speed(0)
    colors = ["blue", "cyan", "gold", "gray", "green", "magenta", "navy", "orange", "orchid", "pink", "purple", "red", "violet", "yellow"]
    count = 1
    # options for colors
    print("The color may be:")
    for color in colors:
        print(f"{count}. {color}")
        count += 1
    print("Enter 0 for black")

    choice = inputchecker(count-1)
    # check if the color they chose is valid
    if choice == 0:
        return drawer
    else:
        drawer.color(color[choice-1])
        return drawer
    # return the drawing object

    
def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
            
    return choicevar