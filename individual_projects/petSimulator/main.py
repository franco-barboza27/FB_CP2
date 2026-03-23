# FB Pet Simulator

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

# PETS SHOULD HAVE
    # Name, species, age, EXP, rank, happiness(fraction), hunger(fraction), thirst(fraction), health(fraction), athletics, beauty, family tree(list)

# Time conversion : 1 hour IRL = 1 day IGL

# MAIN main menu

    # Ask them to create a new game or load a save

    # if loading a save:
        # check if there are any save files (out of 3) that exist
    # otherwise:
        # ask what save they want to start their game in

def main():
    print("Welcome to the friendly Pet Simulator!")

    print("1. Start a new game\n2. Load a save")

    choice = inputchecker(2)

    match choice:
        case 1:
            print("Great! Let's start a new game!")
            newsave = input("What would you like to name your save file? (Do worry, you CAN'T change it later!):\n")

            save = newsavefile(newsave) #new save/tutorial function

        case 2:
            print("Great! Let's load a save!")
            print("Here are your save files:")

            with open("individual_projects\petSimulator\saves.txt", mode="r") as file:
                saves = []
                reader = file.readlines()

                for line in reader:
                    saves.append(line.strip())
            print(f"1. {saves[0]}\n2. {saves[1]}\n3. {saves[2]}")

            choice = inputchecker(3)
            loadsave(choice) #load save function
# loading a save

    # get the save file
    # for every pet in the save
        # for every item in the save
            # save the item to a list
        
        # make the pet a class object with all of the information (from the list made previously)

# CREATING a save

    # ask what file they want to save to
        # create a file with that name
            # add a tutorial pet called "first pet"
        
        # make the first pet a class object

# either way, go to the main GAME loop

# Game Loop

    # Display the menu
        # 1. View pets
        # 2. Breed pets
        # 3. Play a contest
        # 4. Grocery store
        # 5. pets store

    # 1. view pets
        # display every pet name, age and health
        # select or menu
        # selecting
            # display selected pet's information (with turtle, and ASCII)
            # ask if they want to
                # 1. feed
                # 2. play
                # 3. train
                # 4. groom
    
    # 2. breeding pets
        # ask what species they would like to breed (cat, dog, or rabbit)
            # display all pets owned that have that as their species (if only one, say they cannot breed a new animal because they only have the one)
            
            # ask what two they would like to breed
            # make a new pet of the pet class with a random sprite from ONE of the parents
            # add the pet to the list of pets owned

    # 3. play a contest
        # ask what species they would like to play a contest in (cat, dog, or rabbit)
            # display all pets owned that have that as their species (if none, say they cannot play a contest because they do not have any pets of that species)
                # otherwise ask what pet they would like to play a contest with
                # choose a random competitor (with a random sprite)
                # add up the stats of the pet
                # add up the stats of the competitor
                # roll a random number between 0 and 2 (including decimals)
                    # cut the number to the nearest hundredth
                    # multiply the number by the sum of the stats of the pet
                # do the same for the competitor

                # if the pet's number is higher than the competitor's, they win
                    # add EXP to the pet
                    # if the pet's EXP is high enough(according to the rank requirements), they rank up
                    
                    # give them 10 dollars
                # otherwise, they lose
                    # give them 2 dollars

                # go to menu

    # 4. grocery store
        # display their money amount.
        
        # ask if they would like to buy food or water.

        # if food:
            # display the food options (with prices--food replenishment, and happiness increase)
            # ask what they would like to buy
                # if they have enough money, add the item to their inventory and subtract the money from their total
                # otherwise, say they do not have enough money
        # if water:
            # display the water options (with prices--thirst replenishment)(Ex: 12 Oz 1 dollar(20 thirst), 16 Oz 2 dollars(30 thirst), 20 Oz 3 dollars(40 thirst))
            # ask what they would like to buy
                # if they have enough money, add the item to their inventory and subtract the money from their total
                # otherwise, say they do not have enough money
                # sen them to the grocer menu

        # if leaving, go to main game menu

    # 5. pets store
        # display their money amount.
        # display 3 categories of pets (cat, dog, rabbit)
            # ask what category they would like to buy from
                # display the pets available for purchase in that category (with prices, and stats)
                # ask what pet they would like to buy
                    # if they have enough money, 
                        # Ask what they would like to name the pet
                            # add it to their pet list and subtract the money from their total
                    # otherwise, say they do not have enough money
                        # send them to the pet store menu