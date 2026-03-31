# Grade view loop
import codeclasses

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
    currentclass = codeclasses.schoolClass(classname)
    for student in students:
        student = codeclasses.student(student["id"], student["name"], student["gradepercent"], student["gradeletter"], student["gradelevel"], student["gradeavg"], student["academicstanding"])
        currentclass.addstudent(student)

def gradebookloop(students):
    while True:
        print("What would you like to do?")
        print("1. Add student, 2. Add grade, 3. View student record, 4. View all students, 5. Class summary")
        choicevar = inputchecker(5)
        match choicevar:
            case 1:
                addstudent(students)
            case 2:
                addgrade(students)
            case 3:
                viewstudentrecord(students)
            case 4:
                viewallstudents(students)
            case 5:
                classsummary(students)
