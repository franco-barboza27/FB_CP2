# FB Pet Simulator

# in the sprites CSV, the 1st 3 are dogs, the next 3 are cats, the last 3 are rabbit sprites

# PETS SHOULD HAVE
    # Name, species, age, exp, rank, happiness(fraction), hunger(fraction), thirst(fraction), health(fraction), athletics, beauty, family tree(list)

from helpers import *
from gameloop import *
from csvsetup import *

# MAIN main menu

    # Ask them to create a new game or load a save

    # if loading a save:
        # check if there are any save files (out of 3) that exist
    # otherwise:
    54       # ask what save they want to start their game in

 # gamemenu function

def main():
    print("Welcome to the friendly Pet Simulator!")

    print("1. Start a new game\n2. Load a save")

    choice = inputchecker(2)

    match choice:
        case 1:
            print("Great! Let's start a new game!")
            newsave = input("What would you like to name your save file? (Do worry, you CAN'T change it later!):\n")

            newsave = newsave.replace(".", "") # replace periods with nothing to make not break .csv

            user, pets, savepath = newsavefile(newsave) # new save function

        case 2:
            print("Great! Let's load a save!")
            print("Here are your save files:")

            saves = savesgetter()

            count = 1
            for save in saves.keys():
                print(f"{count}. {save}")
                count += 1

            choice = inputchecker(count-1)
            user, pets, savepath = loadsave(list(saves.keys())[choice-1]) # load save function-

    gamemenu(user, pets, savepath)
  
main()