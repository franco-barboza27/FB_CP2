# Write to notes

content = []
with open("notes/filenotes.txt", 'r+') as file:
    for line in file:
        content.append(line.strip())
    
    index = content.index('Thing 3')
    content[index] = "THING 159kjs"
    file.truncate(0)

    for name in content:
        file.write(name + "\n")

print("run finished")

with open("notes/filenotes.txt", 'r') as file:
    content = [file.read(),]
    for line in file:
        content.append(line.strip())

for line in content:
    print(line)