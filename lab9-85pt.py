# 85 pt version

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

myList = [102,98,96,101,100,99,103,97,98,105]

# Insert for loop here
num = 0
newList = []
for a in myList:
    if [num] > 100:
        newList.append(a)
        print newList
    num = num + 1
# This should print [102,101,103,105]
print newList
