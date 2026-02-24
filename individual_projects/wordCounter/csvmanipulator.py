# import CSV
import csv

# datamaker FUNCTION
    # check if there is stuff inside of the .csv file
        # if there isn't:
            # create empty database
    
        # if there is,
            # read the csv
                # add each line and item in each line as an item in a list of dictionaries

def datamaker():
    try:
        with open("individual_projects/wordCounter/docdetails.csv", mode="r") as file:
            files = []
            reader = csv.reader(file)

            for line in file:
                for line in reader:

                    if line:
                        files.append({})


                        thispath = line[0]
                        thisdate = line[1]
                        thiscount = line[2]

                        files[-1]["File path"] = thispath
                        files[-1]["Last updated"] = thisdate
                        files[-1]["Word count"] = thiscount
    except:
        files = [{"File path":"file path example", "Last updated":"example update date", "Word count":"example word count"}]
    
    return files

# data-saver FUNCTION (database, new item)
    # go over every item in the database,
        # check if it's file path and the currently edited file match
            # if they do, replace the current item's information with the new information
        # if there aren't any matches:
            # add the item to the end of the database

    # replace the old CSV file with the database (which would be the same) and the additional value

def datasaver(filebase, fileneeded):
    files = []

    if not filebase:
        filebase.append(fileneeded)

    for file in filebase:
        if file["File path"] == fileneeded["File path"]:
            file = fileneeded.copy()
        else:
            continue
        
        files.append(file["File path"])
    
    if fileneeded["File path"] in files:
        filebase.append(fileneeded)
        
    filesaver(filebase)
            
def filesaver(filebase):

    with open("individual_projects/wordCounter/docdetails.csv", mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = ["File path", "Last updated", "Word count"], delimiter=",")
        heading = ["File path", "Last updated", "Word count"]
        writer.writeheader()
        # writer.writerow(file, )
        
        for file in filebase:
            keylings = list(file.keys())
            value = list(file.values())
            writer.writerow({keylings[0]:value[0], keylings[1]:value[1], keylings[2]: value[2]})