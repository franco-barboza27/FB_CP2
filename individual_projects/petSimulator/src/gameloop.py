import datetime, random

from csvsetup import quitting
from classyclasses import *
from helpers import *

def gamemenu(user, pets, save):
    print(f"welcome, {user.username}!")
    #Game Loop

    while True:
        timecheck(user, pets)
        user.lastlogout = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for pet in pets:
            pet.statcheck()
            if pet.health <= 0: # if health reaches 0, die
                pet.death() # death function
                pets.remove(pet) # remove the pet from the pets list

        print(f"The time is currently {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, and you have ${user.money}!")
        print("What would you like to do?")
        print("1. View pets\n2. Breed pets(W.I.P)\n3. Play a contest\n4. Grocery store\n5. Pets store(no takesybackseys)\n6. Save and Quit")

            # Display the menu
        # 1. View pets
        # 2. Breed pets
        # 3. Play a contest
        # 4. Grocery store
        # 5. pets store

        choice = inputchecker(6)

        match choice:
            case 1:
                count = 1
                for pet in pets:
                    print(f"{count}. {pet.view()}") # pet viewer function
                    count += 1

                print("1. Select a pet\n2. Go back to menu")

                choice = inputchecker(2)

                if choice == 1:
                    choice = inputchecker(count-1)

                    selectedpet = pets[choice-1] # selected pet
                    print("Press BACKSPACE to close the opened window and continue.")
                    selectedpet.detailedview() # pet detailed viewer function

                    print(f"You have selected {selectedpet.name}!\nWhat would you like to do with {selectedpet.name}?")
                    print("1. Feed\n2. Play\n3. Train(W.I.P)\n4. Groom(W.I.P)\n5. Sleep\n6. Go back to menu")
                    choice = inputchecker(6)


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
            
                    if choice == 1:
                        if len(user.inventory) == 0:
                            print("You don't have any food or water in your inventory! Go to the grocery store to buy some!")
                            continue
                        print("What would you like to feed them?")
                        foodfed, hunger, thirst = userly.inventoryviewer(user) # inventory viewer function
                        selectedpet.feed(hunger, thirst)
                        user.inventory = user.inventorysubtract(foodfed) # inventory remove function
                    elif choice == 2:
                        selectedpet.play()
                    elif choice == 3:
                        pass # TRAINING FUNCTION GOES HERE __________________________________________________________________________________________________________________________________
                    elif choice == 4:
                        pass # GROOMING FUNCTION GOES HERE _________________________________________________________________________________________________________________________________
                    elif choice == 5:
                        selectedpet.sleep() 
                    elif choice == 6:
                        continue
            case 2:
            # 2. breeding pets
            # ask what species they would like to breed (cat, dog, or rabbit)
                # display all pets owned that have that as their species (if only one, say they cannot breed a new animal because they only have the one)
                
                # ask what two they would like to breed
                # make a new pet of the pet class with a random sprite from ONE of the parents
                # add the pet to the list of pets owned

                pass # BREEDING FUNCTION GOES HERE ______________________________________________________________________________________________________________________________________________________
            case 3:
                print("What species would you like to play a contest in?")
                print("1. Dog\n2. Cat\n3. Rabbit")
                choice = inputchecker(3)

                if choice == 1:
                    species = "dog"
                elif choice == 2:
                    species = "cat"
                elif choice == 3:
                    species = "rabbit"

                speciespets = []
                for pet in pets:
                    if pet.species == species:
                        speciespets.append(pet)
                
                if len(speciespets) == 0:
                    print(f"You don't have any {species} pets to play a contest with! Go breed or buy some!")
                    continue
                
                count = 1
                for pet in speciespets:
                    print(f"{count}. {pet.view()}")
                    count += 1
                choice = inputchecker(count-1)
                selectedpet = speciespets[choice-1]

                win = selectedpet.compete(petgen(species, selectedpet.rank))

                if win:
                    user.money += 10


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
                                # add exp to the pet
                                # if the pet's exp is high enough(according to the rank requirements), they rank up
                                
                                # give them 10 dollars
                            # otherwise, they lose
                                # give them 2 dollars

                            # go to menu


            case 4:
                user.shop()
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
            case 5:
                if user.money < 50:
                    print("You don't have enough money! Come back when tou have 50 Dollas")
                    continue
                print("Would you like to:\n1. Buy a cat\n2. Buy a dog\n3.Buy a rabbit")
                choice = inputchecker(3)
                match choice:
                    case 1:
                        print("There are three cats!")
                        pettype = "cat"
                    case 2:
                        print("There are three dogs!")
                        pettype = "dog"
                    case 3:
                        print("there are three rabbits!")
                        pettype = "rabbit"
                        print("Will you but the first, second, or third?(1,2,3)")
                        
                petone = petly("NONAME",pettype, random.randint(0, 5), 0, "F", random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(0, 20), random.randint(0, 20), {}, [])
                pettwo = petly("NONAME",pettype, random.randint(0, 5), 0, "F", random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(0, 20), random.randint(0, 20), {}, [])
                petthree = petly("NONAME",pettype, random.randint(0, 5), 0, "F", random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(50, 100), random.randint(0, 20), random.randint(0, 20), {}, [])

                choice = inputchecker(3)

                match choice:
                    case 1:
                        pets.append(petone)
                    case 2:
                        pets.append(pettwo)
                    case 3:
                        pets.append(petthree)

                user.money -= 50

                pets[-1].rename()
                

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

            case 6:
                quitting(user, pets, save)