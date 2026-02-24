# replace
# add
# viewer
# count words

def textgetter():

    text = []

    print("\n\n\nEnter the return/enter button twice (without spaces or tabs in between!) to stop typing!")
    print("What will you type:\n")

    while True:
        sentence = input("")

        if sentence == "":
            break

        text.append(sentence)
    
    return text

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
    
    return True

def fileformatter(filepath):
    for character in filepath:
        if character == "\\":
            character = "/"

# REPLACE function

    # CHECK file

    # open the file in mode WRITE
        # for every item in the new text list
            # write the line to the TXT file

def replacer(filepath):

    text = textgetter()

    with open(filepath, mode="w") as file:

        file.truncate()

        for item in text:
            file.write(item)

# ADD function

    # CHECK file

    # open the file in mode APPEND
        # for every item in the list of new text
            # add it to the end of the TXT file

def adder(filepath):

    text = textgetter()
    
    with open(filepath, mode="a") as file:
        
        for item in text:
            file.write(f"\n{item}")

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

def wordcounter(textpath):

    text = textlister(textpath)

    wordcount = 0

    for item in text:
        currentchar = 0
        for character in item:
            if character != " ":
                try:
                    if item[currentchar+1] == " ":
                        wordcount += 1
                except:
                    break
            
            currentchar += 1
    
    return wordcount


# VIEWER function
    # open the file in mode READ
        # loop over every line in the file
            # print the line

def viewer(textpath):

    text = textlister(textpath)

    for item in text:
        print(item)

# TXT database maker
    # open in mode write
        # add each line to a list

def textlister(filepath):

    text = []

    with open(filepath, mode="r", newline="") as file:
        for line in file:
            text.append(line)

    return text