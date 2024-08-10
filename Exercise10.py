# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a
# new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def oddeven(l1,l2):
    new_list = []
    for i in l1:
        if i % 2 !=0:
            new_list.append(i)
    for i in l2:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


r1 = int(input('Enter the range for 1st list : '))
r2 = int(input('Enter the range for 1st list : '))
list1 = []
for i in range(r1):
    x = int(input('Enter elements for list 1 : '))
    list1.append(x)
print(list1)
list2 = []
for i in range(r2):
    x = int(input('Enter elements for list 2 : '))
    list2.append(x)
print(list2)
print('New List')
print(oddeven(list1,list2))


