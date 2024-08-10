#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a=int(input('Enter first number : '))
b=int(input('Enter second number : '))

if a*b<=1000:
    print(f'The Result is {a * b}')
else:
    print(f'The Result is {a + b}')