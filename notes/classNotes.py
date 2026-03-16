# FB Classes notes

# Ex 1:

class Dog:

    #V always goes at the top of the class, sets up the object and it's values
    def __init__(self, name, breed, age):
        self.name = name.capitalize()
        self.breed = breed.capitalize()
        self.age = age
    
    #V built in function that calls when using a print statememt. This code replaces the regular location return when printing with the string returned.
    def __str__(self):
        return f"This is {self.name} it is a {self.breed}, and is {self.age} years old!"


doug = Dog("Doug", "gold retreiver", 13)

print(doug)