# Donal Buggy

# a program to calculate approximate BMI by taking an input value from the user and running a calculation

print('Please enter your weight in kilograms')
weight = int(input())
print('Please enter your height in centimetres')

# converts the centimetre value to a metre value
height = (int(input()) / 100)

# calculates BMI
bmi = weight / (height)**2
bmivalue = round(bmi, 2)
print('Your BMI is ' + str(bmivalue))