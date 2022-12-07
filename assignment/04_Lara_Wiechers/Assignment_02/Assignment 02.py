# task 01 - String length
import random

print('The length of which expression should be measured?')  # prompting user input

input_string = input()
list = ()
length = 0

if input_string == type(str):
    for i in input_string:
        length += 1
    print(length)
else:
    print('Please enter only expressions which belong to the string data type!')

print('The length of which expression should be measured?')  # prompting user input

input_string = input()
length = 0

for i in input_string:
    length += 1
print(length)

# comment: Even integer data types are interpreted as string data types


# task 02 - Largest Element
import random

list = []
elements = 0
maximum = 0

while elements < 10:
    list.append(random.randrange(1, 100, 1))
    elements += 1
    if list[-1] > maximum:
        maximum = list[-1]

print(maximum)
print(list)

# task 03 – Character Frequency

print('Which expression should be evaluated for character frequency?')  # prompting user input

expression = input()
expression.remove(" ", "")                                              # removing whitespaces from the string

print(expression)

# task 04 - Sorted List of Tuples
import random

list_of_tuples = [(random.randrange(1, 100), random.randrange(1, 100), random.randrange(1, 100)) for i in range(10)]

sorted_list_of_tuples = sorted(list_of_tuples, key=lambda x: x[2])

print(sorted_list_of_tuples)

# task 05 - Check Brackets I

expression = input("Enter expression: ")

open_clips = expression.count('(')
closed_clips = expression.count(')')

if open_clips > closed_clips:
	print('Closing clip is missing')

if open_clips < closed_clips:
	print('Opening clip is missing')

if expression[0] == ')':
	print('first clip incorrect')

if expression[len(expression)-1] == '(':
	print('last clip incorrect')

# task 06 - Check Brackets II
xpression = input("Enter expression: ")

opens = {'round': 0, 'square': 0, 'curly':0}
closed = {'round': 0, 'square': 0, 'curly':0}

for character in expression:

	if character == '(':
		opens['round'] += 1

	if character == '[':
		opens['square'] += 1

	if character == '{':
		opens['curly'] += 1

	if character == ')':
		closed['round'] += 1

	if character == ']':
		closed['square'] += 1

	if character == '}':
		closed['curly'] += 1

if opens['round'] > closed['round']:
	print('Closed round bracket missing')

if opens['round'] < closed['round']:
	print('Open round bracket missing')


if opens['square'] > closed['square']:
	print('Closed square bracket missing')

if opens['square'] < closed['square']:
	print('Open square bracket missing')


if opens['curly'] > closed['curly']:
	print('Closed curly bracket missing')

if opens['curly'] < closed['curly']:
	print('Open curly bracket missing')

# task 07 - Queue
print('Input:')  # prompting user input

initial_input = str(input())
list = []

if initial_input == 'next':
    print('There is no expression in the queue!')
else:
    list.append(initial_input)

while len(list) > 0:
    print('Input:')
    next_input = input()

    if next_input == 'next':
        print(list[0])
        del (list[0])

    else:
        list.append(next_input)

# task 8 - unlimited power I
def power(x, n):
	x = x*x

	print(x)

	n = n-1

	if n > 1:
		power(x,n)

power(2,3)


# task 9 - unlimited power II
