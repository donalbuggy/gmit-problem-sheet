# Donal Buggy

# a program to calculate the approximate square root of an entered value

x = float(input("Please enter a positive number: "))

# function to calculate the approx square root
# sets a baseline value (variable y) to use as a comparison
# performs checks against y and either halves it or adds a fraction of the input value (x) to progressively get y closer to the actual square root of the input value
# when the difference between x and y falls within a certain range, the loop ends and the value of y is returned as the approximate square root
def sqrt(X):
    y = 1
    # tests if the difference between input value (x) and y squared is within an acceptable range. Until test1 == True, the loop will iterate
    test1 = (x - (y * y)) < (x * 0.001)
    while not test1:
        if y**2 > x:
            y = y/2
            if (x - (y * y)) < (x * 0.001):
                test1 = True
                # if the value of y after the operation causes test1 to be True, the loop ends
        elif y**2 < x:
            y = y + (x * 0.001)
            if (x - (y * y)) < (x * 0.001):
                test1 = True
        else:
            break
        
    # when the loop ends, returns the rounded value of y
    print("The approximate square root is " + str(round(y, 2)))

sqrt(x)