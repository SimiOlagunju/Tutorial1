#CALCULATOR APPLICATION ASSIGNMENT:  16-02-2022
#Build a calculator application using all you have learnt at the moment.
#The application should be able to carry out arithmetic operations choices that the user choose.

num1 = int(input('Enter number of workers?'))
num2 = int(input('Enter workers work days?'))
op = input('Enter operator ?')

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op ==  '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
elif op == '%':
    print(num1 % num2)
elif op == '//':
    print(num1 // num2)
else:
    print('We have an incomplete record!')
