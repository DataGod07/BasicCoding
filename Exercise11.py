# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

no = int(input('Enter the number : '))
new_list = []
while no > 0:
    x = no % 10
    new_list.append(x)
    no = no//10
new_str = ''
for i in new_list:
    new_str = new_str + str(i) + ' '

print(new_str)
