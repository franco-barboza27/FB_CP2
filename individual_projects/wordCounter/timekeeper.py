# import datetime library
import datetime as d

# time writer FUNCTION
    # using datetime get the current computer's time
        
    # cut off the microseconds and seconds
    # optionally change the format to be : "Year month(as word)__day--hour:minute"

    # return the time!

def timemaker():
    currenttime = d.datetime.now()

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

    formattedtime = timeformatter(times)

    return formattedtime

def timeformatter(times):
    match times[1]:
        case 1:
            times[1] = "January"
        case 2:
            times[1] = "February"
        case 3:
            times[1] = "March"
        case 4:
            times[1] = "April"
        case 5:
            times[1] = "May"
        case 6:
            times[1] = "June"
        case 7:
            times[1] = "July"
        case 8:
            times[1] = "August"
        case 9:
            times[1] = "September"
        case 10:
            times[1] = "October"
        case 11:
            times[1] = "November"
        case 12:
            times[1] = "December"
    
    times[2] = str(times[2]) + ","

    if times[3] > 12:
        times[3] -= 12

        times[4] = f"{str(times[4])}" + " P.M."
    
    times[3] = f"{str(times[3])}" + " :"

    count = 0
    for time in times:
        times[count] = str(time) + " "
        count += 1

    timesstring = "".join(times)   

    return timesstring