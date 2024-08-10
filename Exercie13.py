# Exercise 13: Print multiplication table from 1 to 10

list_num = [1,2,3,4,5,6,7,8,9,10]

for i in list_num:
    print(f'Table of {i}')
    for x in range(1,11):
        print(i*x ,end = ' ')
    print('\n')