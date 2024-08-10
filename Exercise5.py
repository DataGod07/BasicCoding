# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

def num_check(list_v):
    if list_v[0] == list_v[-1]:
        return True
    else:
        return False


list_num = []
sz = int(input('Enter the size of the list : '))
for i in range(sz):
    a = int(input(f'Enter the element {i} for the list : '))
    list_num.append(a)
print(f'result is {num_check(list_num)}')
