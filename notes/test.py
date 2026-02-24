import datetime as d

filebase =[]

filebase[0]

testquestion = "Testing:"

if "ing" in testquestion:
    print(testquestion)

currenttime = d.datetime.now()

print(currenttime)

times = []

currentyear = currenttime.year
currentmonth = currenttime.month
currentday = currenttime.day
currenthour = currenttime.hour
currentminute = currenttime.minute

times.append(currentyear)
times.append(currentmonth)
times.append(currentday)
times.append(currenthour)
times.append(currentminute)

for time in times:
    print(f"{str(time)}\n")