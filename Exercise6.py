# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5
def divby(list_v):
    print('Divisible by 5')
    for x in list_v:
        if x % 5 == 0:
            print(x)


list_num = []
sz = int(input('Enter the size of the list : '))
for i in range(sz):
    a = int(input(f'Enter the element {i} for the list : '))
    list_num.append(a)
divby(list_num)
