# create empty list
numberList = []

print("Enter number (0 to quit)")
enteredNumber = int(input)

# while loop, adding nums to list until 0 is entered
# consulted StackOverflow (https://stackoverflow.com/questions/19057939/add-user-input-to-list) to add user-entered number values to lists
while enteredNumber != 0:
    numberList.append(enteredNumber)
    print("Enter number (0 to quit):")
    enteredNumber = int(input())
print(numberList)

# avg calculation and printing the value as string
average = float(sum(numberList) / len(numberList))
print("The average is " + str(average))