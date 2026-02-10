# FB 1st movie recommender
import csv
import random
import sys

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

# convert list into a database FUNCTION
    # loop over every line in the database file
    # turn it into an item that is a part of a bigger database 
        # Database:
            # itemnum:[title], [genre(s)], [director(s)], [actor(s)], length, rating]

def databasemaker():
    with open("individual_projects\movie.py\datatest.csv", mode="r") as file:

        movies = {}
        reader = csv.reader(file)
        header = next(reader)
        count = 0

        for line in file:
            thismovie = {}
            for line in reader:
                
                thismovie.update(
                {
                    header[0]: line[0],
                    header[1]: line[1],
                    header[2]: line[2],
                    header[3]: line[3],
                    header[4]: line[4],
                    header[5]: line[5]
                }
                )

                count += 1
                movies[count] = (thismovie)

    menu(movies)

# display menu and go to the option they chose (view list, search, exit)

# search FUNCTION
    # display menu of search by: name, genre, director, actor, length
    # ask which ones they would like to do
    # ask what values they want for each filter they chose

    # for every movie in the database
        # match is TRUE
    
        # If the filter is name
            # check if the value is anywhere within the title
                # if it is NOT
                    # set match to FALSE
        
        # if the filter is genre, director or actor
            # if the filter is a list
                # loop over every item
                    # if the value is NOT inside the item at all
                        # set match to FALSE

        # if the filter is length
            # ask if they want for movies of the same, greater, or lesser length
                # if the movie is NOT (<,>,=)
                    # set match to FALSE!!!
        
        # if match is TRUE
            # add the movie to a temp database

    # call the viewer function

def searcher(database):
    print("Search by\n1. Name\n2. Genre\n3. Director\n4. Actor\n 5. Length")
    
    count = 1
    filters = []

    while count < 5:
        print(f"would you like to filter for option {count}?{"enter an option smaller than the option to say NO"}")
        filtersingular = inputchecker(0, count)

        if filtersingular == count:
            filters.append(filtersingular)
        
        count += 1

    if filters[0] = 1:
        name = input("What is the name of this movie?")
    if filters[0] = 2:
        name = input("What is the genre?")
    if filters[0] = 3:
        name = input("What is the name the director")
    if filters[0] = 4:
        name = input("What is an actor in the movie?")
    if filters[0] = 1:
        name = input("What is w?")

    def filtering():
        
        
         

# view the movies FUNCTION
    # if the movies are existent
        # for every movie in the data base
            # print the movie name, and all the other information
    # otherwise:
        # say that there aren't any movies under the specified 



def menu():
    print("1. make a password\n2. leave the program?")
    placevar = inputchecker(2)

    match placevar:
        case 1:
            requirements()
        case 2:
            sys.exit()

databasemaker()