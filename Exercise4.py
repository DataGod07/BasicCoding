# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

str_in = input('Enter String : ')
n = int(input('Enter the no of characters which has to be removed : '))
str_new = ''
for i in range(n, len(str_in)):
    str_new = str_new + str_in[i]

print(str_new)

