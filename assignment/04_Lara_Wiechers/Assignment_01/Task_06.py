#task 06 - Decimal to Octal Conversion

#specific program

print ('Please enter a non-negative integer number!') #asking for users input
input_number = int(input ()) #converting input into integer
remainder = input_number % 8
remainders = []

if input_number < 0:
    print ('Invalid input. Please enter a non-negative integer number!')
    end()

if input_number == 0:
    print (0)

else:
    while remainder != 0:
        remainders.append (input_number % 8)
        input_number = input_number // 8
        remainder = input_number % 8
    print (*remainders [::-1], sep='', end='')
