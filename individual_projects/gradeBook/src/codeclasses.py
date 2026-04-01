import random

# student:
    # initialize student:
        # takes in the students name, ID, current grade in class, grade letter, and grade level(freshman, sophomore, etc.)
        # creates a student object with the students data and "N/A" for the academic and 0.0 for the GPA

    # ADD GRADE METHOD:
        # Takes in: grade (in points), max points, and grade they got
        # multiply the max points by the students current grade average to get the students current points in the class
        # add the grade they got to the students current points
        # add the max points to the assignment max points
        # divide the students current points by the assignment max points to get the students new grade average
        # upd grade avg

    # METHOD for adding a grade:
    # ask for how many points you can get in the class:

    # Ask for the students ID and the grade(in points) they got, and the max points for the assignment:
        # loop over the students in the class object:
            # if the students ID matches the ID in the class object:
                # use the grade ADD method for the student
                    # update the students average and letter grade

# METHOD for viewing a students record:
    # Ask for the students ID:
        # loop over the students in the class object:
            # if the students ID matches the ID in the class object:
                # print the students name, grade average, letter grade, academic standing, and GPA

class schoolClass:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def addstudent(self, student):
        ids = []
        try:
            student.id =int(student.id)
        except:
            if student.id == "N/A":
                pass
            else:
                print("Invalid student ID. Please provide a student with a valid ID.")
                return True

        if student.id.isnumeric():
            if student.id not in ids:
                self.students.append(student)
                return False
        else:
            for stude in self.students:
                ids.append(stude.id)

            while True:
                student.id = random.randint(0, 2000)
                if student.id not in ids:
                    break
                else:
                    continue
            self.students.append(student)
            return True

    def viewallstudents(self):
        for stude in self.students:
            stude.viewSummaryRecord()

    def classSummary(self):
        highestgrade = 0
        lowestgrade = 100
        totalgrades = 0
        count = 0

        for stude in self.students:
            count += 1
            totalgrades += stude.gradepercent
            if stude.gradepercent > highestgrade:
                highestgrade = stude.gradepercent
            if stude.gradepercent < lowestgrade:
                lowestgrade = stude.gradepercent

        if count > 0:
            averagegrade = totalgrades / count
        else:
            averagegrade = 0

        print(f"Class Name: {self.name}")
        print(f"Highest Grade: {highestgrade}")
        print(f"Lowest Grade: {lowestgrade}")
        print(f"Total Students: {count}")
        print(f"Average Grade: {averagegrade}")

# 1. Add student, 2. Add grade, 3. View student record, 4. View all students, 5. Class summary

class student:
    def __init__(self, id, name, gradepercent, gradeletter, gradelevel, gradeavg, academicstanding):
        self.id = id
        self.name = name
        self.gradepercent = gradepercent
        self.gradeletter = gradeletter
        self.gradelevel = gradelevel
        self.gradeavg = gradeavg
        self.academicstanding = academicstanding
    
    def addgrade(self, pointsgot, maxpoints):
        currentpoints = (self.gradeavg / 100) * maxpoints
        currentpoints += pointsgot
        maxpoints += maxpoints
        newgradeavg = (currentpoints / maxpoints) * 100
        self.gradeavg = round(newgradeavg, 2)
    
    def viewDeetRecord(self):
        print(f"Student ID: {self.id}")
        print(f"    Student Name: {self.name}")
        print(f"    Grade Percentage: {self.gradepercent}")
        print(f"    Grade Letter: {self.gradeletter}")
        print(f"    Grade Level: {self.gradelevel}")
        print(f"    Grade Average: {self.gradeavg}")
        print(f"    Academic Standing: {self.academicstanding}")
    
    def viewSummaryRecord(self):
        print(f"Student ID: {self.id}")
        print(f"    Student Name: {self.name}")
        print(f"    Grade Percentage: {self.gradepercent}")
        print(f"    Grade Level: {self.gradelevel}")


# class class:
    # initialize class:
        # takes in the class name = class name
        # students = []
        # creates a class object with

    # add student function:
        # takes in a student object
        # adds the student object to the class students attribute

    # METHOD for viewing the class summary:
        # highest grade is 0
        # lowest grade is 100
        # count is 0 

        # loop over every student in the class object:
            # count + 1
            # add the student's grade average to a list
            # if the students grade average is higher than the current highest grade:
                # update the highest grade to the students grade average
            # if the students grade average is lower than the current lowest grade:
                # update the lowest grade to the students grade average

        # for every grade in the list of grades:
            # add the grade to a total variable
        # divide the total variable by the number of grades to get the average grade for the class

        # print the highest grade, the lowest grade, total students, and the average grade for the class

    # METHOD for viewing all students:
        # loop over the students in the class attribute:
            # print the students name, grade average, letter grade, academic standing, and GPA

