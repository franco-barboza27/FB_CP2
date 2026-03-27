# FB 2nd update Personal Library Program

# upate functions
# was working on making the searcher more decompositioned

import csv
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

# for every item in the first list of the database
    # check if the item exists in the CSV file
        # if it doesnt, add it to the CSV
        # if it does, do nothing

    # create a new database
        # for item in the new database,
            # check if it's inside the OLD database
                # if it's not
                    # delete it from the database (rewrite it)


def filesaver(bookbase):

    with open("individual_projects/libraryUpdate/books.csv", mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = ["title","author","year","genre"], delimiter=",")
        heading = ["title","author","year","genre"]
        writer.writeheader()
        # writer.writerow(file, )
        
        for book in bookbase:
            keylings = list(book.keys())
            value = list(book.values())
            writer.writerow({keylings[0]:value[0], keylings[1]:value[1], keylings[2]: value[2], keylings[3]: value[3]})

# Open up the book file
# make a list of books
# for every line in said file,
    # for ever line in the READER
        # add the book and author details to the books database

# NEVER REUSE THIS CODE PLEASEEEE _________________________________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________________________________________________________________

def databasemaker():

    try:
        with open("individual_projects/libraryUpdate/books.csv", mode="r") as file:

            books = []
            reader = csv.reader(file)

            for line in file:
                for line in reader:

                    if line:
                        books.append({})


                        thisbook = line[0]
                        thisauthor = line[1]
                        thisyear = line[2]
                        thisgenre = line[3]

                        books[-1]["title"] = thisbook
                        books[-1]["author"] = thisauthor
                        books[-1]["year"] = thisyear
                        books[-1]["genre"] = thisgenre

    except:
        books = [{"title":"title example", "author":"example author", "year":1843, "genre":"genre example"}]
    
    return books

# Helper function that checks if they want to go to the menu yet or not
def menuquestion(database):
    while True:
        print("Would you like to:")
        print("1. Go to menu\n2. Not yet")
        answer = inputchecker(2)

        if answer == 1:
            print("Going to the menu")
            menu(database)
            print("\n\n\n")
        elif answer == 2:
            print("Very well.")
            break
        print("\n\n\n")

# add item function
    # display What is the title of this book?  # In the future this can change to the word "work"
    # display Who is this book by?
    # if a book with the exact same information is in the library ask them to try a different book
    # otherwise add the book to the book database
    
    # call the menu
def additems(database):
    while True:
        name = input("What is the title of this book?:\n")
        creator = input("Who is the author of this book?:\n")
        year = input("When was this book published?")
        genre = input("What genre is this book?")

        database.append({})

        database[-1]["author"] = creator
        database[-1]["title"] = name
        database[-1]["year"] = year
        database[-1]["genre"] = genre

        menuquestion(database)

# search for an item function
    # ask if they'd like to search by title or by author
    # if they choose author, ask which author
        # Display all books written by that author
    # if they chose title, ask what the title is
        # display the book and the author(s) who wrote it

    # call the menu
def searcher(database):

    def questioner(catigorytype):
        if catigorytype == "year":
            answer = input(f"What is the publishing {catigorytype} of the book? (Case sensitive):\n")
        else:
            answer = input(f"What is the {catigorytype} of the book? (Case sensitive):\n")
        
        counter = 0
        tracker = 0
        for item in database:
            if item[catigorytype] == answer:
                counter += 1
                print(f"{counter}. {item["title"]} by {item["author"]} published in {item["year"]}, the genre is {item["genre"]}")
            else:
                print("Hmm, Sorry, but we couldn't find the book you were looking for, are you sure it was spelt correctly?")
            tracker += 1

    while True:
        print("Would you like to: \n1. Search by book name \n2. Search by author \n3. Search by year \n4. Search by genre")
        checker = inputchecker(4)

        if checker == 1:
            questioner("title")
                
        elif checker == 2:
            questioner("author")
        
        elif checker == 3:
            questioner("year")
        
        elif checker == 4:
            questioner("genre")
        
        menuquestion(database)

# remove an item function
    # display What is the title of this book?  # In the future this can change to the word "work"
    # display Who is this book by?
    # if a book with the exact same information is in the library say that the book exists
        # Ask them if they really want to remove it
            # if they do, remove it 
            # if they don't, go back to the beggining of the remove item function
    # otherwise ask them to retry it

    # call the menu
def remover(database):
    while True:
        title = input("What is the name of the book?")
        author = input("What is the name of the author?")

        print("Are you sure you want to remove all instances of this specific work from your database?\n1. Yes\n2. No")
        answer = inputchecker(2)
        if answer == 1:
            print("Now deleting and going to menu")
        else:
            print("Ok, going back to menu")
            menu(database)

        counter = 0
        for item in database:
            if item["title"] == title:
                if item["author"] == author:
                    database.pop(counter)
            counter += 1
        
        menuquestion(database)

# view works function
    # count = 1
    # get length of the database
    # for every pair in the booklist
        # display the count. book title and by author
        # add 1 to count
def skimview(database):
    while True:
        listednumber = 0
        databasesize = len(database)
        counter = 0

        while counter in range(0, databasesize):
            listednumber += 1
            try:
                print(f"{listednumber}. {database[counter]["title"]} by {database[counter]["author"]}")
                counter += 1
            except:
                counter += 1
                print("This is the end of the list")
        print("\n\n\n")

        menuquestion(database)

# detailed view FUNCTION
    # Do similar thing done in the other function BUT add genre and publishing year
def detailedview(database):
    while True:
        listednumber = 0
        databasesize = len(database[0])
        counter = 0

        while counter in range(0, databasesize):
            listednumber += 1
            try:
                print(f"{listednumber}. {database[counter]["title"]} by {database[counter]["author"]} published in {database[counter]["year"]}, the genre is {database[counter]["genre"]}")
            except:
                print("This is the end of the list")
            counter += 1
        print("\n\n\n")

        menuquestion(database)

# Menu function
    # Present the list of options (1-3)
    # Ask them which one they want to do
        # check if it's valid
    # call the corresponding function
def menu(database):
    while True:
        print("Which would you like to use? (enter the number of the item)")

        optlist = ["1. Basic view", "2. Detailed view", "3. Search/sort", "4. Add a book", "5. Remove a book", "6. Exit"]

        for item in optlist:
            print(item)

        choice = inputchecker(6)
        print("\n\n\n")

        if choice == 1:
            print("Opening basic view")
            skimview(database)
        elif choice == 2:
            print("Opening detailed view")
            detailedview(database)
        elif choice == 3:
            print("Opening sort menu")
            searcher(database)
        elif choice == 4:
            print("Going to the Item Addition menu")
            additems(database)
        elif choice == 5:
            print("Going to the Item Removal menu")
            remover(database)
        else:
            print("Are you certain you want to terminate the program? Doing so will also save all changes.")
            print("1. Yes\n2. No")
            terminatequestion = inputchecker(2)
            if terminatequestion == 1:
                filesaver(database)
                sys.exit()
            else:
                print("Very well, going back to the menu.")

print("Hello, this is a book database!\nThe main point of it is to store books and their authors inside of one library.")
books = databasemaker()

menu(books)