# FB 2nd Password Generator
import sys

# input checking function
    # Loop until otherwise:
        # ask which item wanted
        # try to turn it into a number
            # if that doesn't work retry the loop
        # if it is in the range of the allowed inputs break the loop
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

# Menu FUNCTION:
    # display the option list (1.generate a password, 2. exit program)

    # call the input checker

    # if they chose to generate
        # call the generator function
    # if they chose to exit
        # leave the program
def menu():
    print("1. make a password\n2. leave the program?")
    placevar = inputchecker(2)
# requisite asker FUNCTION
    # always looping
        # ask for the length of the password

        # try turning it into an integer
            # if it works, break the loop
            # otherwise keep looping

    # for every item in given list
        # ask if they would like to do the item
            # add their answer as an item to a different list

    # return answer list

# generator FUNCTION
    # call requisite function
    
    # current length of password is 0

    # Helper generator FUNCTION
        # if the number is X,
            # check the Xnd item in the requisites list is true
                # choose a random number in the range of the 1st number in the Xs value and the 2nd number
                # add it to a list
        # return list

    # loop 4 times
        #   while the current length list is in the range of the first value in req.
            # choose a random number between one and 4 (dictionary with X key and ASCII range value)
            # call the helper generator as variable
            
            # current length = variable^ length

        # for every item in the variable, turn it into the ASCII version of the number\
            # add it to a string
        
        # display the string

# Introduce the program, this is a password generator

print("Hello! This is a password generator.")