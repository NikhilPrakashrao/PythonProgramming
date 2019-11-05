"""SCOPE:
1: Read the input given by the user
"""
print("Enter the number")
input_number=input()
print("The number is",input_number)
print(type(input_number))
input_number=int(input_number)
if(input_number>10):
    print("It is greater than 10")
else:
    print("It is less than 10")
