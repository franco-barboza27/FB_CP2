# FB Financial Calculator P.2

# 1. Menu func
    # Present the list of options (2-6)
    # Ask them which one they want to do
        # check if it's valid
    # call the corresponding function

# 2. Savings Time Calculator
    # Ask how much they want to save as a rounded FLOAT VAR
    # Ask how often they are putting in money (daily, biweekly, weekly, bimonthly, monthly, yearly)
        # check if it's valid
    # Ask how much money they are inserting
    # Divide the total they need by the total they amount they are adding
    # say that # is the amount of the time frames they need (that they chose, line 11)

    # optionally: convert time frame to every other time frame and present it in that form as well (e.g. Amount:100, inserting: 10, timeframe: monthly, "It will take ten months, or 40 weeks, or .83 years, or 80 biweeks, or ~300 days")
    # return to the menu
# 3. Compound Interest Calculator
    # Ask how much interest they have
    # Ask the amount of money they have
    # Ask how long they'll leave it alone
    # ask how often it compounds
    # convert interest into a percent (in decimal form)
    # make a loop that repeats the amount of time they'll leave it alone
        # every loop:
            # increase is money * interest
            # add increase to money
    # when loop ends, display info (e.g. "in # of time frame with interest, you will have #$")
    # return to menu func

# 4. Budget Allocator
    # ask how much money they have
    # ask how many categories they have
    # loop that many times with each time displaying "category #" (with number increasing by 1, starting at 1 every loop)
        # ask how what the category is
        # save it in a dictionary as a category:amount spent pair (which should be 0 at first)
    # ask how much they spend in each category (loop over each pair)
        # update every pair to the amount
    # inner function
        
# 5. Sale Price Calculator

# 6. Tip Calculator 


# Checks if it's valid
def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices})")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
            
    return choicevar