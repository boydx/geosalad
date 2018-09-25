
# Get a contour value
contour = input("Enter elevation contour value: ")

# Catching syntax error
# Try converting the string to the number
try: 
    # convert string type to int
    contourNumber = int(contour)
    # if successful, the below step is skipped
    # if unsuccessful the below statement is executed and the program stops
except: # except clause
    print("Not a number! Run program again.")
    exit() # exit function to prevent continuing

# Catching logic errors
# Check to see if contour value is valid for Kentucky
if contourNumber > 4139 or contourNumber < 257:
    print("Elevation outside range! Run program again.")
    exit()
else:
    print("OK! Got good numbers. Lets go!")

# Check to see if it's a contour and if it's an index contour
if contourNumber%40 == 0: 
    if contourNumber%200 == 0:
        print("Your value of " + str(contourNumber) + " is an index contour!")
    else:
        print("You have a contour!")
else:
    print("Sorry. Not an index contour.")

# Tell them we are done!
print("All done!")