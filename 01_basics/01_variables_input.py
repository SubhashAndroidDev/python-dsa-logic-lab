""" problem Add Two Numbers

 input 10,20
 output 30
 -think first
 we need three thinks
 number1
 number2
 result=number1+ number2
"""
# Take the first number from the user.
# input() always returns text, so we convert it to int.
number1=int(input("Enter first number:"))
# take the second number.
number2=int(input("Enter second number:"))

# add both numbers
result=number1+number2

print(f'Sum : {result}')

'''
Enter first number:25
Enter second number:36
Sum : 61
'''
