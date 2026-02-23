# replace
# add
# viewer
# count words

# FILE TYPE checker

    # check the type of the file (make sure it is a .txt)

        # if it isn't, go back to the main main menu, otherwise continue

def filetypecheck(filepath):
    try:
        with open(filepath, mode='r') as file:
            readering = [file.read(),]
        
        if ".txt" not in filepath:
            errormaker = 598
            stringer = "this will cause an error"

            error = errormaker + stringer
    except:
        return False

# REPLACE function

    # CHECK file

    # open the file in mode WRITE
        # for every item in the new text list
            # write the line to the TXT file

def replacer(filepath, text):

    with open(filepath, mode="w") as file:

        file.truncate[0]

        for item in text:
            file.write(item)

# ADD function

    # CHECK file

    # open the file in mode APPEND
        # for every item in the list of new text
            # add it to the end of the TXT file

def adder(filepath, text):
    
    with open(filepath, mode="a") as file:
        
        for item in text:
            file.write(text)

## wow! time for the actual assignment name!

# WORD COUNTER function
    
    # CHECK file 

    # open file in mode READ

        # word counter is 0

        # for every line in the file,
            # for every character in the line
                # check if the character is NOT a space:
                    # if it is not a space:
                        # check if the NEXT character IS
                            # if it is, add 1 to the word counter
                    # if it is a space, go on to the next letter
def wordcounter(text):

    wordcount = 0

    for item in text:
        currentchar = 0
        for character in item:
            if character is not " ":
                if item[currentchar+1] == " ":
                    wordcount += 1
            
            currentchar += 1
    
    return wordcount


# VIEWER function
    # open the file in mode READ
        # loop over every line in the file
            # print the line

def viewer(text):
    for item in text:
        print(item)