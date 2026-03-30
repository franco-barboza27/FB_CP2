# STUDENTS SHOULD BE STORED IN *CODE* AS {id1:{name:name, grade%avg:num, gradeletter:letter, Grade:num}, id2:...}
    # where id is a unique number (which will be ensured when creating a student, and so will that they exist in the students CSV)
import math
import csv, pathlib

# Initializing the class/students:

def classGet(classname):
    basepath = pathlib.Path(__file__).resolve().parent
    filepath = basepath.parent / 'resources' / 'classesHolder' / f'{classname}.csv' 
    with open(filepath, "r") as f:
        students = []
        reader = csv.reader(f)
        for line in reader:
            if line:
                try:
                    students.append({})

                    thisname = line[0]
                    thisid = line[1]
                    thisgradeavg = line[2]
                    thisgradeletter = line[3]
                    thisgrade = line[4]

                    students[-1]["name"] = thisname
                    students[-1]["id"] = thisid
                    students[-1]["gradeavg"] = thisgradeavg
                    students[-1]["gradeletter"] = thisgradeletter
                    students[-1]["gradelevel"] = thisgrade

                except:
                    print("There aren't any students in this class yet :(")
                    return []
        
    gradeavgGet(students)

    return students
    # Get Students FUNCTION:
            # the CHOSEN class file:
            # read every line
                # try to:
                    # create a dictionary with the header of the CSV as the keys and the individual student data as the values
                    # add it to a list
                # otherwise:
                    # say there arent any students :(

            # open the Grade Average GET FUNCTION
            
            # open Dict To Objects FUNCTION

def gradeavgGet(students):
    for student in students:
        classes = ["amCiv", "chemistry", "english", "CompSci2", "math"]

        for classfile in classes:
            basepath = pathlib.Path(__file__).resolve().parent
            filepath = basepath.parent / 'resources' / 'classesHolder' / f'{classfile}.csv' 
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                for line in reader:
                    if line:
                        try:
                            if student["id"] in line:
                                grade = float(line[2])
                                maxgrade = float(line[3])
                                totalpoints += grade
                                totalmaxpoints += maxgrade
                        except:
                            continue
        
        if totalmaxpoints != 0:
            gradeavg = totalpoints/totalmaxpoints
            student["gradeavg"] = gradeavg

    # Grade Average GET
        # get the classes from the Reading the Classes FUNCTION
        # get students in the class

        # for every student
            # get the student's ID, add it to a list

        # OPEN the students file
            # for every line:
                # Create a dictionary item where the ID is the key, and the value is a list of their GPA and their Academic Standing

        # for every student in class ID:
            # for every student with GPA ID:
                # if the two IDs match:
                    # Add the GPA as another item in the student

    # Dict To Objects:
        # for every student in the students dictionary:
            # create a student object with the students data
            # add it to a list of student objects

# Saving students to :
    # Dict To CSV:
        # open the current class file
        # write the header of the CSV
        # for every student in the class object:
            # write the students data to the CSV in the correct format

    # Grade Average CALC FUNCTION
        # for every student in the class object:
            # for every class in classes:
                # open the class file:
                    # read every line:
                        # if the students ID is in the line:
                            # get the students grades
                            # calculate the average
                            # add it to the students data