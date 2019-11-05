"""SCOPE:
1:Get the input from user
2:use the input to calculate the Body Mass Index
"""
height=input("Enter the height in Meters\n")
weight=input("Enter the weight in kilograms\n")
height=float(height)
weight=int(weight)
bmi=(weight/(height*height))
print(bmi)
if(bmi<16):
    print("The person is underweight")
elif(bmi>16 and bmi<25):
    print("The person is normal")
elif(bmi>25 and bmi<40):
    print("The person is overweight")
else:
    print("The person is obese")

