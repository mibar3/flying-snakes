import random
count = 0
list_tuples = []
while count < 10:
  count1 = 0
  tuple1 = []
  while count1 < 3:
    x = random.randint(1, 100)
    tuple1.append(x)
    count1 += 1
  count += 1
  list_tuples.append(tuple(tuple1))
print(list_tuples)
list_tuples.sort()
print('The list of tuples sorted:', list_tuples)
