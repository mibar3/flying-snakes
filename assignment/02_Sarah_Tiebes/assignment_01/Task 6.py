# Task 6:Decimal to octal Conversion

print('Name a Number')
dez_number = float(input())

while dez_number < 0:
    (print('Error'))
    dez_number= float(input())

i = 0
oct_number=[]

# conversion: dec to oct

while (dez_number > 0):
    rest = dez_number % 8
    oct_number.insert(i, rest)
    i=i+1
    dez_number = int(dez_number/8)

i = i-1
while i >= 0:
    print(oct_number[i], end='')
    i = i-1
print()
