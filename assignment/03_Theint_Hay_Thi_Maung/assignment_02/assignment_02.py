"""Task 01 – String Length
Write a program that reads in a string and prints the length of the input string.
Do not use any built-in functions of Python, such as len().
For example, if the input is “Computer Science”, the output should be length: 16."""

input_string = input("Please enter the string")
length = 0
for x in input_string:
    length = length + 1
print(length)

'''Task 02 – Largest List Element Write a program that generates a list of 10 random integers between 1 and 100 and 
then finds and prints the largest element in the list. Do not use the built-in function max(). For example, 
if the input is [23,3,42,29,12,15,8,4,37,34], the output should be the largest element: 42. Hint: Check out the 
module random. '''

import random

number = random.sample(range(1, 100), 10)
print(number)
max = number[0]
for i in range(len(number)):
    if number[i] > max:
        max = number[i]
    else:
        i = i + 1
print(max)

'''Task 03 – Character Frequency
Write a program that:
Reads in a string and removes any spaces from the string
Counts how often individual characters occur in the string
Stores the information on character occurrence frequency in a dictionary
Prints the dictionary.
For example, if the input is “santa claus”, the output should be: {'s': 2, 'a': 3, 'n': 1, 't': 1, 'c': 1, 'l': 1, 'u': 1}.'''

input_string = input("Please enter the string")
string = input_string.replace(' ', '')
count_dist = {}
for i in string:
    if i in count_dist.keys():
        count_dist[i] = count_dist[i] + 1
    else:
        count_dist[i] = 1
print(count_dist)

'''Task 04 – Sorted List of Tuples
Write a program that:
Generates a list of 10 tuples, each tuple consisting of 3 random integers between 1 and 100
Sorts the list of tuples in increasing order of the third element in each tuple
Prints the sorted list of tuples
For example, if the generated input list is: [(56, 77, 69), (43, 30, 38), (2, 77, 101), (93, 57, 4), (74, 21, 77), (39, 68, 68), (65, 53, 96), (16, 29, 88), (88, 70, 38)] The output should be: [(93, 57, 4), (43, 30, 38), (88, 70, 38), (39, 68, 68), (56, 77, 69), (74, 21, 77), (16, 29, 88), (65, 53, 96), (2, 77, 101)]
Hint: You are allowed and encouraged to use built-in functions, such as sorted(), for this task.'''

res = []
import random

for i in range(0, 10):
    rand = random.sample(range(1, 100), 3)
    res.append((rand[0], rand[1], rand[2]))
# print(res)
sorted_list = sorted(res, key=lambda x: x[2])
print(sorted_list)

'''Task 05 – Check Brackets
Write a program that reads in a string, which is supposed to be a mathematical expression. Focus on brackets only and check whether left and right brackets are composed correctly. Ignore all other characters (i.e. you don’t have to check correctness of operators and operands). Examples of correct input:
3*(2+5)
((()())())
(3+)(((4)))
Empty string
Examples of incorrect input:
(3*(2+5)
((()())(())
(3+)((4)))
())(()'''

input_string = input("Please enter the mathematical expression string")
openbracket = 0
closebracket = 0
for i in input_string:
    if i == '(':
        openbracket = openbracket + 1
    elif i == ')':
        closebracket = closebracket + 1
if openbracket == closebracket:
    print("Correct input")
else:
    print("Incorrect input")

'''Task 06 – Check Brackets II
Extend previous program, so it can handle also square and curly brackets. Note that expressions in brackets cannot overlap. 
So, expression {[()()]([[]])}{} is correct, but expression ([)] is not.'''

input_string = input("Please enter the mathematical expression string")
dist = {}
for i in input_string:
    if i in dist.keys():
        dist[i] = dist[i] + 1
    else:
        dist[i] = 1

if ('(' in dist) & (')' in dist) & ('[' in dist) & (']' in dist) & ('{' in dist) & ('}' in dist):
    if (dist['('] == dist[')']) & (dist['['] == dist[']']) & (dist['{'] == dist['}']):
        print("Correct input")
    else:
        print("Incorrect input")
else:
    print("Incorrect input")

'''Task 07 – Queue
Write a program that simulates a queue. It will read strings from the input. 
Consider these inputs as names of people coming to the end of a queue. Whenever “next” is given as input, the program will print out the name on the turn. 
The program finishes as soon as the queue is empty.'''

queue = []
while True:
    names = input("write names. If you want to stop type next")
    if names != 'next':
        queue.append(names)
        continue
    else:
        for i in range(len(queue)):
            # print(queue[-1])
            print(queue.pop(0))
        break

'''Task 08 – Unlimited Power
Write a function with two arguments –  𝑥  and  𝑛 . The function returns the value of  𝑥𝑛 . Use recursion.'''


def power(x, n):
    if n == 0:
        return 1
    elif n >= 1:
        return x * power(x, n - 1)


# print(power(3,2))

'''Task 09 – Unlimited Power II
Using function for factorial and function  𝑥𝑛  from previous task, write a program that reads value of  𝑥  and prints approximate value of  𝑒𝑥 . Use this formula (Taylor series) for calculation
𝑒𝑥=1+𝑥+𝑥22!+𝑥33!+...+𝑥𝑛𝑛! 
To get precise value of  𝑒𝑥 , the series would have to be infinite. Suppose that there is some required accuracy, so the calculation finishes as soon as the value of the next element is smaller than given threshold (e.g., 0.000001).'''


def factorial(x):
    if x == 0:
        return 1
    elif x >= 1:
        return x * factorial(x - 1)


def unlimited_power(n):
    value = 0
    if n == 0:
        return 1
    elif n >= 1:
        for i in range(0, n):
            value = value + n ** i / factorial(i)
        return value


unlimited_power(3)
