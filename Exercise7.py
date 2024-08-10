# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.
ct = 0
str_x = "Emma is good developer. Emma is a writer"
List_str = str_x.split(' ')
str_w = input('Enter the word for search : ')
for i in List_str:
    if i == str_w:
        ct = ct + 1
print(f'{str_w} appeared {ct} times')
