# Grade view loop
from turtle import rt

from codeclasses import *
from helpers import *
from initialize import *

# display menu:
    # 1. Add student
    # 2. Add grade
    # 3. View student record
    # 4. View all students
    # 5. Class summary

# FUNCTION for adding a student:
    # Ask for the students name, ID, current grade in class, grade letter, and grade level(freshman, sophomore, etc.):
        # create a student object with the students data and "N/A" for the academic and 0.0 for the GPA
        # add the object to the class object

def gradebookstartup(students, classname):
    currentclass = schoolClass(classname)
    count = 0
    for stude in students:
        if count !=0:
            studeupd = student(stude["id"], stude["name"], stude["gradepercent"], stude["grade letter"], stude["grade"], stude["gradeavg"], stude["academicstanding"])     
        count += 1
        try:
            currentclass.addstudent(studeupd)
        except:
            pass
    
    gradebookloop(currentclass)

def gradebookloop(currentclass):
    while True:
        print("What would you like to do?")
        print("1. Add student\n2. Add grade\n3. View student record\n4. View all students\n5. Class summary\n6.Save and Quit")
        choicevar = inputchecker(6)
        match choicevar:
            case 1:
                while True:
                    name = input("What is this student's name?")
                    # Grade ask, checks that grade is a valid number
                    while True:
                        try:
                            grade = int(input("What is this student's grade percent?"))
                            if 0 <= grade <= 100:
                                break
                            else:
                                print("Please enter a grade between 0 and 100.")
                        except ValueError:
                            print("Please enter a valid integer for the grade.")
                    
                    print("Does this student already have an ID?\n1. Yes \n2. No")
                    choice = inputchecker(2)
                    if choice == 1:
                        id = input("What is this student's ID?")
                    else:
                        id = "N/A"

                    print("What grade is this student in?")
                    gradelevel = input("Enter the student's grade level: ")

                    if grade >= 90:
                        gradeletter = "A"
                    elif grade >= 80:
                        gradeletter = "B"
                    elif grade >= 70:
                        gradeletter = "C"
                    else:
                        gradeletter = "F"

                    stude = student(id, name, grade, gradeletter, gradelevel, 00, "N/A")
                    try:
                        studecorrect = currentclass.addstudent(stude)
                        if not studecorrect:
                            print("Student added successfully.")
                            break
                    except:
                        print(f"An error occurred while adding the student: 61 gradeLoop")
            case 2:
                while True:
                    studeid = input("What is the student's ID?")
                    if studeid:
                        break
                    else:
                        print("Please enter a valid student ID.")
                for stude in currentclass.students:
                    if stude.id == int(studeid):
                        print("How many points the student get:")
                        points = integercheck()
                        print("How many points can they get on the assignment?")
                        totalpoints = integercheck()
                        print("How many max points can you get in the class CURRENTLY(and not including this assignment):")
                        maxpoints = integercheck()
                        stude.addgrade(points, totalpoints, maxpoints)
                print("List finished.")
            case 3:
                while True:
                    studeid = input("What is the student's ID?")
                    if studeid.isdigit():
                        break
                    else:
                        print("Please enter a valid student ID.")
                for stude in currentclass.students:
                    try:
                        if stude.id == int(studeid):
                            stude.viewDeetRecord()
                    except:
                        print("there was and error: 85")
            case 4:
                currentclass.viewallstudents()
            case 5:
                currentclass.classSummary()
            case 6:
                saveStudents(currentclass.students,currentclass.name)