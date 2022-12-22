import random
count = 0
number10 = []
while count < 10:
  number = random.randint(1, 100)
  number10.append(number)
  count += 1
print(number10)
number10.sort()
print('The largest element in the list is:', number10[-1])
