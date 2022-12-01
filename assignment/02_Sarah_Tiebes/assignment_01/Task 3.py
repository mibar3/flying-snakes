# Task 3: Fibonacci Numbers

Number = int(input('Name an upper bound:'))

F0 = 0
F1 = 1
count = 0

if Number <= 0:
    print('Please but in a positive number')
elif Number == 1:
    print('Fibonacci sequence upto' + Number + ':')
    print(F0)
else:
    print('Fibonacci sequence:')
    while count <= Number:
        print(F0)
        next_number = F0 + F1
        F0 = F1
        F1 = next_number
        count = F0
