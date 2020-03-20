# consulted tutorialspoint.com (https://www.tutorialspoint.com/python/number_round.htm) to use Python round() method

# used a  single instance of round() at point of input to test for decimal numbers, instead of using a separate if statement for each if/elif below
print("Please enter your percentage grade:")
studentGrade = round(float(input()))

if studentGrade < 0 or studentGrade > 100:
    print("Invalid value")

if studentGrade >= 0 and studentGrade < 40:
    print("Fail")

elif studentGrade >= 40 and studentGrade <= 49:
    print("Pass")
elif studentGrade >= 50 and studentGrade <= 59:
    print("Merit 2")
elif studentGrade >= 60 and studentGrade <=69:
    print("Merit 1")
elif studentGrade >= 70 and studentGrade <= 100:
    print("Distinction")
