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
    with open("individual_projects/movieFolder/movies.csv", mode="r") as file:

        movies = {}
        reader = csv.reader(file)
        header = next(reader)
        count = 0

        for line in file:
            for line in reader:
                
                thismovie ={
                    header[0]: line[0],
                    header[1]: line[1],
                    header[2]: line[2],
                    header[3]: line[3],
                    header[4]: line[4],
                    header[5]: line[5]
                }
        

                count += 1
                movies[count] = thismovie
    
    filterreadier(movies)

# makes a copy of the database, and then strip and lowercaseify every single value

def filterreadier(moviebase):

    chars_to_remove = " ,/-':;|}]{[=+_>.<!@#$%^&*()"
    table = str.maketrans("", "", chars_to_remove)

    searchermoviebase = moviebase.copy()

    for diction in moviebase:
        searchermoviebase[diction] = moviebase[diction].copy()

    movieskeys = list(searchermoviebase.keys())
    moviedetailkeys = list(searchermoviebase[1].keys())

    for key in movieskeys:

        for detail in moviedetailkeys:

            text = searchermoviebase[key][detail]
            lowertext = text.casefold()
            strippedtext = lowertext.translate(table)

            searchermoviebase[key][detail] = strippedtext

    menu(moviebase, searchermoviebase)

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

def searcher(database, stripped):

    filters = []

    def answers(question):
        while True:
            requi = input(f"{question}(Input 0 to skip):\n")
            if requi:
                break

        filters.append(requi)

    questions = ["What is the name of this movie?", "What is the genre?", "What is the name the director", "What is an actor in the movie?"]

    for ques in questions:
        answers(ques)

    strippedfilters = []

    for filter in filters:
        if filter != "0":
            chars_to_remove = " ,/-':;|}]{[=+_>.<!@#$%^&*()"
            table = str.maketrans("", "", chars_to_remove)
            filter = filter.casefold()
            filter = filter.translate(table)

        strippedfilters.append(filter)
    
    filters = strippedfilters

    def filtering(filters, database, stripped):

        viewingbase = {}

        keysofstripped = list(stripped[1].keys())

        tracker = 1

        for movie in stripped:
            matching = True
            count = 0

            for filter in filters:

                keyval = keysofstripped[count]

                if filter != "0":
                    if filter not in stripped[movie][keyval]:
                        matching = False

                count += 1

            if matching == True:
                viewingbase.update({tracker:database[tracker]})

            tracker += 1
        
        viewer(database, stripped, viewingbase)

    filtering(filters, database, stripped)

# view the movies FUNCTION
    # if the movies are existent
        # for every movie in the data base
            # print the movie name, and all the other information
    # otherwise:
        # say that there aren't any movies under the specified 
def viewer(movies, strippedata, dataviewed):

    keys = list(dataviewed.keys())
    count = 0

    for movie in dataviewed:
        count += 1
        print(f"{count}. ")
        for value in dataviewed[movie]:
            try:
                print(f" -  {value} : {dataviewed[movie][value]}")
            except:
                print("aw dangit!")
    
    try:
        print(dataviewed[1])
    except:
        print("Hmmmm, it seems that there aren't any movies under those requirements... how unfortunate")

# display menu and go to the option they chose (view list, search, exit)

def menu(movies, strippedmovies):
    while True:
        print("1. View movies\n2. Search\n3. leave the program?")
        placevar = inputchecker(3)

        match placevar:
            case 1:
                viewer(movies, strippedmovies, movies)
            case 2:
                searcher(movies, strippedmovies)
            case 3:
                sys.exit()

databasemaker()