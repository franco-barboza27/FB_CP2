import csv

try:
    with open("notes/filenotes.txt", "r") as file:
        content = [file.read(),]
        for line in file:
            content.append(line.strip())
except:
    print("Cannoy find the file :(")
else:
    for line in content:
        print(line)

try:
    with open("notes/CSVtestfile.csv", mode= "r") as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[0]
                }
            )
except:
    print("OH NO! ERROR")
else:
    for user in users:
        print(user)