print("Please enter your percentage grade:")
studentGrade = int(input())

# if statement to ensure the grade is within a valid range
if studentGrade < 0 or studentGrade > 100:
    print("Invalid value")

# if statement to check fail range
if studentGrade >= 0 and studentGrade < 40:
    print("Fail")

# elif statements to check the subsequent grade ranges
elif studentGrade >= 40 and studentGrade <= 49:
    print("Pass")
elif studentGrade >= 50 and studentGrade <= 59:
    print("Merit 2")
elif studentGrade >= 60 and studentGrade <=69:
    print("Merit 1")
elif studentGrade >= 70 and studentGrade <= 100:
    print("Distinction")
