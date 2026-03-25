from helpers import *
import turtle
import random

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

    def rename(self):
        newname = input("What would you like your pet's new name to be?")
        newname.replace(",", "")
        newname.replace(".", "")

        self.name = newname

    def feed(self, hunger, thirst):
        self.hunger += hunger
        self.thirst += thirst
        self.health += (thirst+hunger)*.5
        self.happiness += (thirst+hunger)*.25
        self.health = round(self.health)

        print(f"{self.name}'s health increased by {(thirst+hunger)*.5}! Happiness also increased by {(thirst+hunger)*.25}!")
        self.statcheck()

    def healthchange(self, change):
        self.health += change
        self.statcheck()
    
    def view(self):
        return f"{self.name}\n    {self.age} years old\n    Species: {self.species}\n    Rank: {self.rank}\n    Health: {self.health}%\n    Hunger: {self.hunger}%\n    Thirst: {self.thirst}%"
    
    def detailedview(self):
        details = f"{self.name}\n    {self.age} years old\n    Species: {self.species}\n    Rank: {self.rank}\n    exp: {self.exp}\n    Health: {self.health}%\n    Hunger: {self.hunger}%\n    Thirst: {self.thirst}%\n    Happiness: {self.happiness}%\n    Athletics: {self.athletics}\n    Beauty: {self.beauty}\n"
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
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger > 100:
            self.hunger = 100
        if self.thirst > 100:
            self.thirst = 100
        if self.health > 100:
            self.health = 100
        if self.athletics > 100:
            self.athletics = 100
        if self.beauty > 100:
            self.beauty = 100

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
            inventory = str(self.inventory[item][0])+str(self.inventory[item][1])
            hunger = int(inventory[0]+inventory[1])
            thirst = int(inventory[2]+inventory[3])

            print(f"{count}. {item} : Hunger--{hunger}, Thirst--{thirst}")
            count += 1
        
        print("You may select an item")
        choice = inputchecker(count-1)
        itemname = list(self.inventory.keys())[choice-1]

        return itemname, hunger, thirst
    
    def inventorysubtract(self, food):
        self.inventory.pop(food)
        
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
            count += 1
        
        choice = inputchecker(count-1)
        foodname = list(foods.keys())[choice-1]
        foodstats = [int(foods[foodname][0] + foods[foodname][1]), int(foods[foodname][2] + foods[foodname][3])]
        cost = round((foodstats[0]+foodstats[1])*.5)

        foodbought = {}
    
        if foodname in self.inventory.keys():
            print("You already have this item! Use it first and then come back to buy it i you want!")
        elif self.money >= cost:
            self.money -= cost
            foodbought[foodname] = foodstats
            self.inventoryadd(foodbought)
            print(f"You bought {foodname} for ${cost}!")
        else:
            print("You don't have enough money to buy that! Go earn some more by playing contests!")

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