# FB Pet Simulator

# in the sprites CSV, the 1st 3 are dogs, the next 3 are cats, the last 3 are rabbit sprites

import pathlib
import datetime
import turtle
import random

def strlistconvert(string):
    strlist = []
    tempstr = ""
    for char in string:
        if char != ",":
            tempstr = f"{tempstr}"+f"{char}"
        else:
            strlist.append(tempstr)
            tempstr = ""

    return strlist

def listdictconvert(listitem):
    dictversion = {}
    for item in listitem:
        keypair = item.split(":")
        dictversion[keypair[0]] = keypair[1]

    return dictversion

def petgen(species, rank):
    pet = []
    names = [f"Jake's {species}", f"Molly's {species}", f"Charlie’s {species}", f"Bella's {species}", f"Max's {species}", f"Lucy’s {species}", f"Rocky's {species}", f"Daisy's {species}", f"Toby's {species}"]
    ranks = ["F", "E", "D", "C", "B", "A", "S"]

    if species == "dog":
        sprite = pet.append(random.randint(1, 3))
    elif species == "cat":
        sprite = pet.append(random.randint(4, 6))
    elif species == "rabbit":
        sprite = pet.append(random.randint(7, 9))

    rankgrade = ranks.index(rank)+1

    health = 100
    hunger = 100
    thirst = 100
    happiness = 50
    athletics = round(rankgrade * 10 * (random.random()+.1))
    beauty = round(rankgrade * 10 * random.random())
    exp = 0
    age = random.randint(0, 20)
    familytree = []
    skills = {"Smell":f"This pet can smell things around them!"}
    name = random.choice(names)

    return petly(name, species, age, exp, rank, happiness, hunger, thirst, health, athletics, beauty, skills, familytree)

class petly:
    def __init__(self, name, species, age, exp, rank, happiness, hunger, thirst, health, athletics, beauty, skills, familytree, sprite=None):
        self.name = name
        self.species = species
        self.age = int(age)
        self.exp = int(exp)
        self.rank = rank
        self.sprite = sprite
        self.happiness = int(happiness)
        self.hunger = int(hunger)
        self.thirst = int(thirst)
        self.health = int(health)
        self.athletics = int(athletics)
        self.beauty = int(beauty)

        skills = strlistconvert(skills)
        skills = listdictconvert(skills)
        self.skills = skills
        
        familytree = strlistconvert(familytree)
        self.familytree = familytree

    def feed(self, hunger, thirst):
        self.hunger += hunger
        self.thirst += thirst
        self.health += (thirst+hunger)*.5

        self.health = round(self.health)

        self.statcheck()

        return self.hunger, self.thirst, self.health

    def healthchange(self, change):
        self.health += change
        self.statcheck()
    
    def view(self):
        return f"{self.name}\n    {self.age} years old\n    Species: {self.species}\n    Rank: {self.rank}\n    Health: {self.health}%\n    Hunger: {self.hunger}%\n    Thirst: {self.thirst}%"
    
    def detailedview(self):
        details = f"{self.name}\n    {self.age} years old\n    Species: {self.species}\n    Rank: {self.rank}\n    EXP: {self.exp}\n    Health: {self.health}%\n    Hunger: {self.hunger}%\n    Thirst: {self.thirst}%\n    Happiness: {self.happiness}%\n    Athletics: {self.athletics}\n    Beauty: {self.beauty}\n"
        print(details)
        for skill in self.skills.keys():
            print(f"{skill}: {self.skills[skill]}")
        
        writer = turtle.Turtle()
        writer.up()
        writer.hideturtle()

        treesize = len(self.familytree)

        writer.goto(-250* round(.9**treesize), 250 * round(.9**treesize))

        count = 0
        for i in range(len(self.familytree)):
            count += 1
            writer.write(self.familytree[-1-i], font=("Arial", 50*round(.5**treesize), "normal"))
            if count % 2 != 0:
                writer.goto(writer.xcor() + 100* round(.9**treesize), writer.ycor())
            elif count % 2 == 0:
                writer.goto(-250 - 50* round(.9**treesize), writer.ycor() - 50* round(.9**treesize))
        
        writer.goto(writer.xcor() + 50, writer.ycor() + 20)
        
        writer.write(self.name, font=("Arial", 50*round(.5**treesize), "normal"))
        
        turtle.Screen().onkey(lambda: turtle.Screen().clear(), "BackSpace")

    def play(self):
        print(f"You went to the park with {self.name}!")
        self.encounter()
        print(f"Happiness increased by 10, and athletics by 5!")
        print(f"After having fun playing at the park, {self.name} is feeling great!")
        print(f"Although, now it's time to head home.")
    
    def encounter(self):
        encchance = random.randint(1, 10)
        match encchance:
            case 1:
                print(f"{self.name} encountered a friendly animal!")
            case 2:
                print(f"{self.name} found a tasty treat!")
            case 4:
                print(f"{self.name} met a new friend!")
            case 6:
                print(f"{self.name} found a stick!")
            case 7:
                print(f"{self.name} had a fun adventure!")

        self.happiness += 20
        self.athletics += 5

        self.statcheck()

    def statcheck(self):
        for stat in (self.happiness, self.hunger, self.thirst, self.health, self.athletics, self.beauty):
            if stat > 100:
                stat = 100

        newskills = {"Run":f"{self.name} can run around the park!", "Jump":f"{self.name} can jump over small obstacles!", "Swim":f"{self.name} can swim in the lake!", "Fetch":f"{self.name} can fetch a ball!", "Dig":f"{self.name} can dig holes in the ground!", "roll over":f"{self.name} can roll over!"}
        
        if self.exp >= 50:
            self.exp = 0
            ranks = ["F", "E", "D", "C", "B", "A", "S"]
            if self.rank != "S":
                self.rank = ranks[ranks.index(self.rank)+1]
                print(f"{self.name} has ranked up to {self.rank}!")
                
                for skill in newskills.keys():
                    if skill not in self.skills.keys():
                        self.skills[skill] = newskills[skill]
                        newskill = skill
                        
                        break
                
                print(f"{self.name} has learned a new skill: {newskill} : {self.skills[newskill]}!")

            else:
                print(f"{self.name} is already at the highest rank.")
            
        if self.hunger <= 0 or self.thirst <= 0:
            self.hunger = 0
            self.thirst = 0
            self.health = 0
            print(f"{self.name} has died from neglect!")
    
    def death(self):
        print(f"This kind of thing takes a while. How could you let {self.name} die? They were your friend! :(((")
        # remove the pet from the pets list in the main game loop
        # maybe add a function to remove the pet from the pets list here? idk if that would work or if it would cause problems with the timecheck function

    def sleep(self):
        print(f"{self.name} is sleeping... zzz...")
        self.hunger -= 10
        self.thirst -= 10
        self.health += 10

        self.statcheck()

    def compete(self, competitor):
        score = self.athletics + self.beauty + (self.health*.5)
        competitorscore = competitor.athletics + competitor.beauty + (competitor.health*.5)

        if score > competitorscore:
            print(f"{self.name} won the contest against {competitor.name}!")
            self.exp += 10
            self.statcheck()
            return True
        else:
            print(f"{competitor.name} won the contest against {self.name}!")
            return False   

class userly:
    def __init__(self, username, money, lastlogout, inventory):
        self.username = username
        self.money = money
        self.lastlogout = lastlogout

        inventory = strlistconvert(inventory)
        inventory = listdictconvert(inventory)
        self.inventory = inventory
    
    def inventoryviewer(self):
        count = 1
        for item in self.inventory.keys():
            hunger = self.inventory[item][0] + self.inventory[item][1]
            hunger = int(hunger)
            thirst = self.inventory[item][2] + self.inventory[item][3]
            thirst = int(thirst)

            print(f"{count}. {item} : Hunger--{hunger}, Thirst--{thirst}")
            count += 1
        
        print("You may select an item")
        choice = inputchecker(count-1)
        itemname = list(self.inventory.keys())[choice-1]
        hunger = self.inventory[itemname][0] + self.inventory[itemname][1]
        thirst = self.inventory[itemname][2] + self.inventory[itemname][3]

        return itemname, hunger, thirst
    
    def inventorysubtract(self, food):
        items = self.inventory.keys()

        for item in items:
            if item == food:
                self.inventory.pop(item)
        
        return self.inventory

    def inventoryadd(self, food):
        foodname = list(food.keys())[0]
        foodstats = list(food.values())[0]
        self.inventory[foodname] = foodstats

    def shop(self):
        foods = {"Small Pet Food":"2010", "Medium Pet Food":"4015", "Large Pet Food":"5020", "12 Oz Water":"1020", "16 Oz Water":"1540", "20 Oz Water":"1550"}
        print(f"Welcome to the shop! You have ${self.money}.")
        print("What would you like to buy?")
        count = 1
        for food in foods.keys():
            cost = round((int(f"{foods[food][0]}"+f"{foods[food][1]}")+int(f"{foods[food][2]}"+f"{foods[food][3]}"))*.5)
            print(f"{count}. {food} : Hunger Replenishment: {foods[food][0]}{foods[food][1]}----Thirst Replenishment: {foods[food][2]}{foods[food][3]} -- Cost: ${cost}")
            print(int(f"{foods[food][0]}"+f"{foods[food][1]}"))
            print(int(f"{foods[food][2]}"+f"{foods[food][3]}"))
            count += 1
        
        choice = inputchecker(count-1)
        foodname = list(foods.keys())[choice-1]
        foodstats = [int(foods[foodname][0] + foods[foodname][1]), int(foods[foodname][2] + foods[foodname][3])]
        print(foodstats)
        cost = round((foodstats[0]+foodstats[1])*.5)

        foodbought = {}
    
        if self.money >= cost:
            self.money -= cost
            foodbought[foodname] = foodstats
            self.inventoryadd(foodbought)
            print(f"You bought {foodname} for ${cost}!")
        else:
            print("You don't have enough money to buy that! Go earn some more by playing contests!")

def timecheck(user, pets):
    try:
        user.lastlogout = user.lastlogout.replace(microsecond=0, tzinfo=None) # remove microseconds and timezone information from the last logout time to make it easier to compare with the current time
    except:
        pass

    if user.lastlogout != datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"): # if the last logout time is not the same as the current time (which it shouldn't be)

        lastlog = datetime.datetime.strptime(f"{user.lastlogout}", "%Y-%m-%d %H:%M:%S") # convert the last logout time to a datetime object
        now = datetime.datetime.now() # get the current time as a datetime object
        timegone = now - lastlog # calculate the time gone as a timedelta object
        
        timegone = timegone.total_seconds() / 3600 # convert the time gone to hours

        for pet in pets: # for every pet, update their stats based on how long they have been gone
            pet.hunger = pet.hunger - 0.5 * timegone # decrease hunger by .5 for every hour gone
            pet.thirst = pet.thirst - 0.5 * timegone # decrease thirst by .5 for every hour gone

            pet.healthchange(-2 * (0.5 * timegone)) # change the pet's health based on their hunger and thirst
    
    return user, pets

def savesgetter():

    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'saves.csv'
    with open(filepath, mode="r") as file:
        saves = {}
        reader = file.readlines()
        for line in reader:
            save = line.split(",") # split the line into save name and save file path
            saves[save[0]] = save[1] # use the first element as the key and second as value (save name and save info)

    return saves

# loading a save

    # get the save file
    # for every pet in the save
        # for every item in the pet info
            # save the item to a list
        
        # make the pet a class object with all of the information (from the list made previously)

def loadsave(savefileinfo):
    saves = savesgetter()
    pets = []
    user = {}

    for save in saves.keys():
        if save == savefileinfo:
            print(f"Loading {save}...")
            # get the save file path from the saves dictionary
            savefilepath = saves[save]
            # open the save file and read the information

            with open(savefilepath, mode="r") as file:
                reader = file.readlines()
                count = 0
                for line in reader:
                    count += 1
                    if count == 2:
                        userinfo = line.split(",")

                        user = userly(userinfo[0], userinfo[1], userinfo[2], userinfo[3]) # make the user a class object with all of the information (from the list made previously)
                    else:
                        petinfo = line.split(",") # split the line into pet information
                        thispet = petly(petinfo[0], petinfo[1], petinfo[2], petinfo[3], petinfo[4], petinfo[5], petinfo[6], petinfo[7], petinfo[8], petinfo[9], petinfo[10], petinfo[11], petinfo[12]) # make the pet a class object with all of the information (from the list made previously)
                        pets.append(thispet) # add the pet information to the pets list
                        
                    # make the pet a class object with all of the information (from the list made previously)

    return user, pets
                
def newsavefile(newsave):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / (newsave+'.csv')
    with open(filepath, mode="w") as file:
        file.write(f"{newsave}, {filepath}\n") # add the new save to the saves file

    username = input(f"Enter your username:\n")

    with open(basepath.parent / 'resources' / (newsave+'.csv'), mode="w") as file: # create the new save file
        file.write("Name, species, age, EXP, rank, happiness, hunger, thirst, health, athletics, beauty, skills, family tree\n") # write the pet information categories to the save file
        file.write(f"{username}, {0}, {datetime.datetime.now()}, {{}}\n") # write the user information categories to the save file

    user = userly(username, 40, datetime.datetime.now(), {}) # make the user a class object with all of the information (from the list made previously)
    petname = input("What would you like to name your first pet?:\n")
    firstpet = petly(petname, "dog", 0, 0, "F", 50, 100, 100, 100, 10, 10, {}, []) # make the first pet a class object with all of the information (from the list made previously)
    
    pets = []
    pets.append(firstpet)

    return user, pets

# CREATING a save

    # ask what file they want to save to
        # create a file with that name
            # add a tutorial pet called "first pet"
        
        # make the first pet a class object

# either way, go to the main GAME loop
    
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

            newsave = newsave.replace(",", "") # replace commas with nothing to make not break csv

            user, pets = newsavefile(newsave) # new save function

        case 2:
            print("Great! Let's load a save!")
            print("Here are your save files:")

            saves = savesgetter()

            count = 1
            for save in saves.keys():
                print(f"{count}. {save}")
                count += 1

            choice = inputchecker(count-1)
            user, pets = loadsave(list(saves.keys())[choice-1]) # load save function-

    gamemenu(user, pets) # gamemenu function

def gamemenu(user, pets):
    print(f"welcome, {user.username}!")

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
        print("1. View pets\n2. Breed pets(W.I.P)\n3. Play a contest\n4. Grocery store\n5. Pets store")
        choice = inputchecker(5)

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

                    if choice == 1:
                        if len(user.inventory) == 0:
                            print("You don't have any food or water in your inventory! Go to the grocery store to buy some!")
                            continue
                        print("What would you like to feed them?")
                        foodfed, hunger, thirst = userly.inventoryviewer(user) # inventory viewer function
                        selectedpet.hunger, selectedpet.thirst, selectedpet.health = selectedpet.feed(hunger, thirst) # feed function
                        user.inventory = user.inventoryremove(user, foodfed) # inventory remove function
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
                selectedpet = pets[choice-1]

                win = selectedpet.compete(petgen(species, selectedpet.rank)) # compete function with a randomly generated competitor of the same species and rank as the selected pet

                if win:
                    user.money += 10

            case 4:
                user.shop() # shop function

                


                
                
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

main()