# FB Grade book
from helpers import *
import sys
import initialize
import gradeloop
# Display Welcoming

# Ask if they would like to begin the program
    # if yes:
        # GOTO initialize
            # from initialize, get all the current classes existing
        # ask which class they want to go to
            # GOTO initialize
                # from initialize, get the students for the class they chose
                # GOTO gradeloop
    # if no: exit program

# MAKE A FUNCTION/PART THAT CHECKS IF A FILE BEING CREATED BY THE USER IS ALREADY EXISTANT ! ! ! !


def main():
    print("Welcome to the grade book!")

    while True:
        print("Would you like to begin the program? (1 for yes, 2 for no)")
        choicevar = inputchecker(2)
        if choicevar == 1:
            print("Great! Which class would you like to go to?")
            print("1. American HIstory, 2. English, 3. Math, 4. Chemistry, 5. Computer Science")
            classchoice = inputchecker(5)
            match classchoice:
                case 1:
                    classchoice = "amCiv"
                case 2:
                    classchoice = "english"
                case 3:
                    classchoice = "math"
                case 4:
                    classchoice = "chemistry"
                case 5:
                    classchoice = "CompSci2"

            students = initialize.studentGet(classchoice)
            gradeloop.gradebookstartup(students, classchoice)
            
        else:
            print("Okay, goodbye!")
            sys.exit()

main()