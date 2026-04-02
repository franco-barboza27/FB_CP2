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

def integercheck():
    while True:
        num = input("Please enter a number value:")
        try:
                nnum = int(num)
                num = nnum
                break
        except ValueError:
            continue
    
    return num 