# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
str_in = input('Enter String > ')
len_str = len(str_in)
for i in range(len_str):
    if i % 2 == 0:
        print(str_in[i])
