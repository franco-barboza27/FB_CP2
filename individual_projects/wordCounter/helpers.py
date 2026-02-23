# input checking function from a previous project
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

# TXT database maker
    # open in mode write
        # add each line to a list

def textlister(filepath):

    text = []

    with open(filepath, mode="r") as file:
        for line in file:
            text.append(line)