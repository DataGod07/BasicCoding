# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
def exponent(b,e):
    res = b**e
    return res


b = int(input('Enter the base : '))
e = int(input('Enter the exponent: '))
r = exponent(b,e)
print(f'{b} to the power {e} is {r}')


