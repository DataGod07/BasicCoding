# Exercise 8: Print the following pattern

for i in range(6):
    x = i
    i = str(i)
    print(i*x)


for i in range(6):
    for j in range(i):
        print(i,end=' ')
    print('\n')
