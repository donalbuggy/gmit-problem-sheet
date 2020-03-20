import random

# create the empty list to hold the generated random numbers, then generate the list and print it as a string
tenRandoms = []
for i in range(10):
    tenRandoms.append(random.randint(0, 100))
print("Ten random numbers: " + str(tenRandoms))

# sort the list into descending order (largest number to smallest)
# consulted python.org (https://wiki.python.org/moin/HowTo/Sorting) to use the sort() function
tenRandoms.sort(reverse = True)

# create the empty list to hold the three highest numbers, then print that list as a string also
topThree = []
for i in range(0, 3):
    topThree.append(tenRandoms[i])
print("The top three are " + str(topThree))