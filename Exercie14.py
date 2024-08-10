# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
list_num = [5,4,3,2,1]
for i in list_num:
    print('*  '*i)
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")