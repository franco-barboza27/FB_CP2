import csv, pathlib, datetime
import sys
from classyclasses import *

def quitting(user, pets, path):
    with open(path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = ["name","species","age","exp","rank","happiness","hunger","thirst","health","athletics","beauty","skills","familytree"], delimiter=",")
        heading = ["name","species","age","exp","rank","happiness","hunger","thirst","health","athletics","beauty","skills","familytree"]
        writer.writeheader()
        # writer.writerow(file, )
        
        writer.writerow({"name": user.username,"species": user.money,"age": user.lastlogout,"exp": f"'{user.inventory}'","rank": 0,"happiness": 0,"hunger": 0,"thirst": 0,"health": 0,"athletics": 0,"beauty": 0,"skills": 0,"familytree": 0})

        for pet in pets:
            writer.writerow({"name": pet.name,"species": pet.species,"age": pet.age,"exp": pet.exp,"rank": pet.rank,"happiness": pet.happiness,"hunger": pet.hunger,"thirst": pet.thirst,"health": pet.health,"athletics": pet.athletics,"beauty": pet.beauty,"skills": f"'{pet.skills}'","familytree": f"'{pet.familytree}'"})

    sys.exit()


def savesgetter():
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'save.csv'
    with open(filepath, mode="r") as file:
        saves = {}
        reader = file.readlines()
        count = 0
        for line in reader:
            if line and count != 0:
                save = line.split(",") # split the line into save name and save file path
                saves[save[0]] = save[0] # use the first element as the key and second as value (save name and save path)
            count += 1

    return saves

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
            basepath = pathlib.Path(__file__).resolve().parent
            filepath = basepath.parent / 'resources' / f'{savefilepath}.csv'
            with open(filepath, mode="r") as file:
                reader = file.readlines()
                user = []
                count = 0
                for line in file:
                    for line in reader:
                        count += 1
                        if count == 1:
                            if line:
                                user.append({})

                                thisname = line[0]
                                thismoney = line[1]
                                thisdate = line[2]
                                thisinventory = line[3]

                                user[-1][thisname] = thisname
                                user[-1][thismoney] = thismoney
                                user[-1][thisdate] = thisdate
                                user[-1][thisinventory] = thisinventory

                                newuser = userly(user[thisname], user[thismoney], user[thisdate], user[thisinventory])

                                # Name, species, age, exp, rank, happiness, hunger, thirst, health, athletics, beauty, skills, family tree
                        else:
                            pet = []
                            pet.append({})

                            thisname = line[0]
                            thisspecies = line[1]
                            thisage = line[2]
                            thisexp = line[3]
                            thisrank = line[4]
                            thishappiness = line[5]
                            thishunger = line[6]
                            thisthirst = line[7]
                            thishealth = line[8]
                            thisathletics = line[9]
                            thisbeauty = line[10]
                            thisskills = line[11]
                            thisfamilytree = line[12]

                            pet[-1]["name"] = thisname
                            pet[-1]["species"] = thisspecies
                            pet[-1]["age"] = thisage
                            pet[-1]["exp"] = thisexp
                            pet[-1]["rank"] = thisrank
                            pet[-1]["happiness"] = thishappiness
                            pet[-1]["hunger"] = thishunger
                            pet[-1]["thirst"] = thisthirst
                            pet[-1]["health"] =thishealth
                            pet[-1]["athletics"] =thisathletics
                            pet[-1]["beauty"] =thisbeauty
                            pet[-1]["skills"] = thisskills
                            pet[-1]["familytree"] =thisfamilytree

                            newpet = petly(pet[-1]["name"],pet[-1]["species"],pet[-1]["exp"],pet[-1]["rank"],pet[-1]["happiness"],pet[-1]["hunger"],pet[-1]["thirst"],pet[-1]["health"],pet[-1]["athletics"],pet[-1]["beauty"],pet[-1]["skills"],pet[-1]["familytree"])
                            pets.append(newpet) # add the pet information to the pets list
                        
                    # make the pet a class object with all of the information (from the list made previously)

    return newuser, pets, savefilepath

# loading a save

    # get the save file
    # for every pet in the save
        # for every item in the pet info
            # save the item to a list
        
        # make the pet a class object with all of the information (from the list made previously)
                
def newsavefile(newsave):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / (newsave+'.csv')
    savespath = basepath.parent / 'resources' / 'save.csv'
    with open(savespath, mode="w") as file:
        file.write(f"{newsave}, {filepath}") # add the new save to the saves file

    with open(savespath, mode='r+') as file:
        fileinfo = []
        reader = csv.reader(file)

        for line in file:
            for line in reader:

                if line:
                    fileinfo.append({})

                    thisname = line[0]
                    thispath = line[1]

                    fileinfo[-1][thisname] = thispath
    
    check = 0
    for item in fileinfo:
        if newsave in item.keys():
            check = True
            break
        else:
            check = False
    
    if check == False:
        fileinfo.append({})
        fileinfo[-1][newsave] = filepath
    
    with open(savespath, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames = ["savename","filepath"], delimiter=",")
        heading = ["savename","filepath"]
        writer.writeheader()
        # writer.writerow(file, )
        
        for info in fileinfo:
            keylings = []
            value = []

            keylings.append(list(info.keys())[0])
            value.append(list(info.values())[0])
            
            writer.writerow({"savename":keylings[0], "filepath":value[0]})

    username = input(f"Enter your username:\n")

    with open(filepath, mode="w") as file: # create the new save file
        file.write("Name, species, age, exp, rank, happiness, hunger, thirst, health, athletics, beauty, skills, familytree") # write the pet information categories to the save file
        file.write(f"{username}, {0}, {datetime.datetime.now()}, {{}}") # write the user information categories to the save file

    user = userly(username, 40, datetime.datetime.now(), {}) # make the user a class object with all of the information (from the list made previously)
    petname = input("What would you like to name your first pet?:\n")
    firstpet = petly(petname, "dog", 0, 0, "F", 50, 100, 100, 100, 10, 10, {}, []) # make the first pet a class object with all of the information (from the list made previously)
    
    pets = []
    pets.append(firstpet)

    return user, pets, filepath

# CREATING a save

    # ask what file they want to save to
        # create a file with that name
            # add a tutorial pet called "first pet"
        
        # make the first pet a class object

# either way, go to the main GAME loop