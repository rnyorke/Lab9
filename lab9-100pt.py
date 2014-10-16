#100 pts

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
x = True

while(x):
    print "-----------------------------------------------------------"
    print "What is your temperature?"
    temperature = int(raw_input())
    print "-----------------------------------------------------------"
    print "Have you been sick in the past 24 hours?"
    sick = raw_input()
    print "-----------------------------------------------------------"
    print "Have you travelled to West Africa recently?"
    travel = raw_input()
    print "-----------------------------------------------------------"
    if temperature > 105:
        print "You need to be admitted!"
    elif sick == "yes" and temperature > 102:
        print "You need to be admitted!"
    elif temperature > 100 or sick == "yes":
        if travel == "yes":
            print "You need to be admitted!"
            print "-----------------------------------------------------------"
        else:
            print "You do not need to be admitted!"
    else:
        print "You do not need to be admitted!"
    print "-----------------------------------------------------------"
    print "Are there any more patients?"
    patients = raw_input()
    if patients == "no":
        x = False
    else:
        print "-----------------------------------------------------------"
        print "Next please!"
        print ""
    