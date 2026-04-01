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
    for stude in students:
        studeupd = student(stude["id"], stude["name"], stude["gradepercent"], stude["gradeletter"], stude["gradelevel"], stude["gradeavg"], stude["academicstanding"])
        currentclass.addstudent(studeupd)
    
    gradebookloop(currentclass)

def gradebookloop(currentclass):
    while True:
        print("What would you like to do?")
        print("1. Add student\n2. Add grade\n3. View student record\n4. View all students\n5. Class summary\n6.Save and Quit")
        choicevar = inputchecker(5)
        match choicevar:
            case 1:
                while True:
                    name = input("What is this student's name?")
                    # Grade ask, checks that grade is a valid number
                    while True:
                        try:
                            grade = int(input("What is this student's grade?"))
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
                    student = student(id, name, grade, "N/A", "N/A", 00, "N/A")
                    try:
                        grades = currentclass.addstudent(student)
                        if grades:
                            print("Student added successfully.")
                    except:
                        print(f"An error occurred while adding the student: 59")
            case 2:
                while True:
                    studeid = input("What is the student's ID?")
                    if studeid.isdigit():
                        break
                    else:
                        print("Please enter a valid student ID.")
                for stude in currentclass:
                    if stude.id == int(studeid):
                        stude.addgrade(currentclass, stude)
                print("List finished.")
            case 3:
                while True:
                    studeid = input("What is the student's ID?")
                    if studeid.isdigit():
                        break
                    else:
                        print("Please enter a valid student ID.")
                for stude in currentclass:
                    if stude.id == int(studeid):
                        stude.viewDeetRecord(currentclass, stude)
            case 4:
                currentclass.viewallstudents()
            case 5:
                currentclass.
            case 6:
                saveStudents(currentclass.students,currentclass.name)