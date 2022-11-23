# Task 4: Selective Printing

print('Name me a number:')
Number = int(input())
for x in range(Number + 1):
    if x%3!=0:
        print(x)
    elif x==0:
        print(x)

