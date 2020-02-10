print('Please enter your weight in kilograms')
weight = int(input())
print('Please enter your height in centimetres')
height = (int(input()) / 100)
bmi = weight / (height)**2
bmivalue = round(bmi, 2)
print('Your BMI is ' + str(bmivalue))