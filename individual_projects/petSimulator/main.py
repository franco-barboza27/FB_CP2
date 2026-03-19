# FB Pet Simulator

# PETS SHOULD HAVE
    # Name, species, age, EXP, rank, happiness(fraction), hunger(fraction), thirst(fraction), health(fraction), athletics, beauty, family(list)

# Time conversion : 1 hour IRL = 1 day IGL

# MAIN main menu

    # Ask them to create a new game or load a save

    # if loading a save:
        # check if there are any save files (out of 3) that exist
    # otherwise:
        # ask what save they want to start their game in

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
        # 4. Breed pets
        # 5. Grocery store
        # 6. pets store

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
            # make a new pet of the pet class with a random sprite from one of the parents