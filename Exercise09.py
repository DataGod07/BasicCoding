# Exercise 9: Check Palindrome Number
num_int = int(input('Enter Number '))
ste1 = str(num_int)
num_list = []
while num_int>0:
    x = num_int % 10
    num_list.append(x)
    num_int = int(num_int/10)
ste2 = ''
for i in num_list:
    ste2 = ste2 + str(i)

print(ste1)
print(ste2)

if ste1 == ste2:
    print('Palindrome')
else:
    print('Not Palindrome')