#Task 01 – Hello World!
#Write a simple program that asks the user to input a name and outputs a simple greeting,
# such as ‘Hi Name! Nice to meet you!’ and in the other line, ‘Welcome to the Programing Course!’.
#Hint: Check out the input () and print() function in Python.
name = input("Please write your name:")
print('Hi '+name +'!')
print("Welcome to the Programming Course!")

#Task 02 – Reversed Words
#Write a program that reads in a word provided by the user and prints the word in a reversed order. For example, if the input is hello, the output should be ‘olleh’.
#Use a loop structure
#Use just array indexes
word = input("Please write something")
print(word[::-1]) #[start, stop, step]

#Task 03 – Fibonacci Numbers
#Write a program that reads in an upper bound (number) provided by the user and prints the sequence of Fibonacci numbers that are less or equal to the number given by the user. Use a while-loop for this task.
#The Fibonacci sequence is defined as  𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2 . Use  𝐹0=0  and  𝐹1=1  as seed values.
#For example, if the user inputs 6, the output should be 0, 1, 1, 2, 3, 5.

number = int(input("Please put the number:"))
f0 = 0
f1 = 1
if number <= 0:
  print(f0)
else:
  print(f0, ',' ,f1,end = '')
  for x in range(2,number):
    f_next = f0+f1
    print(',', f_next, end ='')
    f0 = f1
    f1 = f_next


'''Task 04 – Selective Printing
Write a program that reads in an upper bound (number) provided by the user and prints all integer numbers that are less or equal to the upper bound except the integer numbers that are divisible by 3. Use the continue statement. 
For example, if the user enters 6 as the upper bound, the output should be 0, 1, 2, 4, 5.'''

number = int(input("Please put the number:"))
for i in range(0, number, 1):
    if i % 3 != 0:
        print(i)


'''Task 05 – Triangle Checking
Write a Python program that asks the user to input the lengths of the sides in a triangle and outputs whether the triangle is equilateral, isosceles, or scalene. The program should also check for the Triangle inequality  (𝑧<𝑥+𝑦) , and prompt the user for a valid input.
An equilateral triangle is a triangle in which all three sides are of equal length.
An isosceles triangle is a triangle with (at least) two sides of equal length.
A scalene triangle is a triangle in which all three sides have different lengths.
For example, if the user inputs a=3, b=4, c=5, the triangle is scalene.'''

a, b, c = input("Enter three length of triangle by giving space between them:").split()
if a + b > c or b + c > a or a + c > b:
    flag = 1
else:
    flag = 0
while flag == 1:
    if a == b == c:
        print("Equilateral triangle")
        breakpoint
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
        breakpoint
    else:
        print("Scalene triangle")
        break
else:
    print("Plese put the input again")
    a, b, c = input("Enter three length of triangle by giving space between them:").split()

'''Task 06 – Decimal to Octal Conversion
Write a program that reads a non-negative integer number in the decimal representation provided by the user and prints the octal representation of the number. For example, if the user enters 167, the output should be 247.
Write a more general program that reads in a non-negative number (potentially including decimal places) in the decimal representation provided by the user and prints the octal representation of the number. For example, 
if the user enters 25.11, the output should be 31.0702436560507534.'''

decimal = int(input("Enter the non-negative integer number"))
octal = []
i = 0
if decimal < 0:
  print("You didn't put the postivie integer number")
elif decimal == 0:
  print(0)
else:
  while(decimal!=0):
    remainder = decimal % 8
    octal.append(remainder)
    decimal = int(decimal/8)
    i = i+1

octal.reverse()
print(*octal,sep='')
