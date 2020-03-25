# Donal Buggy

# a program to runs the Collatz algorithm. It takes a number from the user and checks if it is odd or even; if even, it divides the number by 2 and returns it; if odd, it multiplies the number by 3 and adds 1 and returns it. The program continues to loop until 1 is returned.

print("Please input a positive integer:")
firstnum = int(input())

# while loop to cancel the calculation when firstnum = 1
while firstnum != 1:

    # if statement to check if firstnum is odd or even, runs appropriate calculation in each case
    if firstnum % 2 == 0:
        firstnum = firstnum / 2
        print(firstnum)
    else:
        firstnum = (firstnum * 3) + 1
        print(firstnum)