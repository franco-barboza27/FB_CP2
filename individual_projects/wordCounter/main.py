# FB 1st word counter

# import the source files
import csvmanipulator as cm
import dochandler as dh
import timekeeper as tk
import helpers as help

# introduce the user to the program (edits docs, saves word count, saves most recent time editted)
print("Hello! This is a document word count and edit date tracker")
print("It can tell you how many words there are in a document AND the most recent time you last editted it at")
print("You can also replace or add new information to documents. It ONLY works as a .txt file though")


# ask them what the file exact file path is to the document they want to do things with
    # or if they'd rather terminate the program

def firstmenu():
    while True:
        file = input("What is the EXACT direct file path to your file?")
        file = dh.fileformatter(file)
        istext = dh.filechecker(file)
        
        if istext == True:
            database = cm.datamaker()
            mainmenu(file, database)
        else:
            print("The file is unfortunately not a TXT or doesn't exist, did you make sure it works?")
    

# MAIN function
    # 1. Update document info
    # 2. View document
    # 3. Add content to document
    # 4. Exit this menu (choose a different file)

    # if updating a document

        # Ask if they're sure they want to, which would replace the old document
            # if not go back to menu, otherwise move on

        # ask what they want to replace it with
            # use the document handler UPDATE function
            # use the document handler WORD COUNT function
            # use the timekeeper to get the current date and time

            # from the CSV manipulator file, use the CSV finder to check if the file path exists inside
                # if it does, create a database of the document paths, word counts, and edits
                    # replace the old (< and ^ done in the csv.py file, expanded on more)
                # if it doesn't
                    # append it normally to the CSV

    # viewing the document
        # dochandler DOC PRINTER function

    # adding to the document
        # dochandler DOC ADDER function

    # go back to the beginning of the main loop

def mainmenu(file, data):
    ask = print("You may: \n1. Update this document \n2. View this document \n3. Add to this document \n4. Switch files \n5. EXIT the program\n")
    answer = help.inputchecker(5)

    match answer:
        case 1:
            dh.docreplace
        case 2:
            dh.docview
        case 3:
            dh.docadd
        case 4

if __name__ == "__main__":
    pass
    # function call