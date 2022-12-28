#task 02 - Reversed Words

#1 version without loop structure
print('What words should I reverse?') #asking for users input
word_to_reverse = input ()
print (word_to_reverse [::-1])

#2 version with loop structure
word_to_reverse = input()
array = []
reversed_array = []

for i in word_to_reverse: #loop for generating array
    array.append(i)

for j in array[::-1]: #loop for generating reversed array
    reversed_array.append(j)

print(reversed_array)
