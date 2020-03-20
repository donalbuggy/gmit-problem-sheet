# define the lists for first names and surnames, and enter first pair of values
firstNames = []
surNames = []
firstName = input("Please enter first name:")
firstNames.append(firstName)
surName = input("Please enter surname:")
surNames.append(surName)

# initiate loop to take in subsequent names
while firstName != "":
    firstName = input("Please enter first name of next student:")
    firstNames.append(firstName)
    surName = input("Please enter surname:")
    surNames.append(surName)

# range over the items in each list to print the first and surnames of each student
print("Here are the students you entered:")
for i in range(len(firstNames)):
    print(firstNames[i] + " " + surNames[i])