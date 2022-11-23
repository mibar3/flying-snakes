# Task 2: reversed Words

print('Write a word:')
Word = input()
reversedString=[]
index = len(Word)
while index > 0:
    reversedString += Word[ index - 1]
    index = index -1
reversedString= ''.join(reversedString)
print(reversedString)
