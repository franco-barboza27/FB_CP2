import datetime, random

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
