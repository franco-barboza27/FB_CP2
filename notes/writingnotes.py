# Write to notes

content = []
"""with open("notes/filenotes.txt", 'r+') as file:
    for line in file:
        content.append(line.strip())
    
    index = content.index('Thing 3')
    content[index] = "THING 159kjs"
    file.truncate(0)

    for name in content:
        file.write(name + "\n")"""

print("run finished")


with open("notes/filenotes.txt", 'a') as file:
    count = 0
    for number in range(1, 101):
        file.write(f"{str(number)}\n")
        count += 1

with open("notes/filenotes.txt", "r") as file:
    numbers = []
    for line in file:
        numbers.append(line)

with open("notes/filenotes.txt", "w") as file:

    for

    
    file.write(numbers)

"""for line in content:
    print(line)"""