import random

number = random.randint(1, 10)
print("The random number is {}".format(number))

print("Please select the minimum number you would like the number to be:")
lowerend = int(input())
print("Please select the maximum nmber you wouldl like the number to be:")
upperend = int(input())
# taking user-submitted integers as the range for the new random number
secondnumber = random.randint(lowerend, upperend)
print("The new random number is {}".format(secondnumber))