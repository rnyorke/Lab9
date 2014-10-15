############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

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
    if temperature > 105:
        print "-----------------------------------------------------------"
        print "You have a fever of " + str(temperature)
    print "-----------------------------------------------------------"
    print "Have you been sick in the past 24 hours?"
    sick = raw_input()
    if sick == "yes":
        if temperature >102:
            print "-----------------------------------------------------------"
            print "you have a cold"
    print "-----------------------------------------------------------"
    print "Have you travelled to West Africa recently?"
    travel = raw_input()
    if temperature > 100 or sick == "yes":
        if travel == "yes":
            print "-----------------------------------------------------------"
            print "You have ebola, time for quarantine!"
    elif temperature <= 100 or sick == "no" or travel == "no":
        print "-----------------------------------------------------------"
        print "You are healthy!!"
    print "-----------------------------------------------------------"
    print "Are there any more patients?"
    patients = raw_input()
    if patients == "no":
        x = False
    else:
        print "-----------------------------------------------------------"
        print "Next!"
        print "-----------------------------------------------------------"
        