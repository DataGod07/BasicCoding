# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers,
# and in each iteration, print the sum of the current and previous number.

for i in range(0, 10):
    sum_num = i+i-1
    if i == 0:
        sum_num = 0
        print(f'Current Number {i} Previous Number {i} SUM: {sum_num}')
    else:
        print(f'Current Number {i} Previous Number {i-1} SUM: {sum_num}')
