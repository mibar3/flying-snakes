# Task 5: Triangle Checking

print('Name the length of each side of a triangle:')
print('side a:')
A = int(input())
while A <= 0:
    (print('Please put in only positive numbers'))
    A = int(input())

print('side b:')
B = int(input())
while B <= 0:
    (print('Please put in only positive numbers'))
    B = int(input())

print('side c:')
C = int(input())
while C <= 0:
    (print('Please put in only positive numbers'))
    C = int(input())


if A >= B + C or B >= C + A or C >= B + A:
    exit(print('Your Triangle is not possible'))
else:
    if A == B == C:
        print('Your Triangle is equilateral')
    elif A == B or B == C or C == A:
        print('Your Triangle is isosceles')
    else:
        print('Your Triangle is selene')
