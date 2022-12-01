#task 04 - Selective Printing

print ('What is the upper bound you want to define?') #asking for users input
upperbound = int(input ())

for x in range(int(upperbound)+1):
    if x % 3 == 0 and x != 0:
        continue
    print (x)
