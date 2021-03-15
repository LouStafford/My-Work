# Weekly Tasks 2
# Author: Louise Stafford
# Program to calculate BMI
# The inputs are the person's height in centimetres and weight in kilograms.
# The output  is their weight divided by their height in metres squared

height = float (input( "please enter height in cm: "))
weight = float (input ("please enter weight in kg: "))
bmi = weight / (height / 100)**2
# round result to two decimal places
print ("BMI is ", round(bmi,2))