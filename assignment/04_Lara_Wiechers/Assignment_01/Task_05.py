#task 05 - Triangle Checking

print ('What is the length of the first side of the triangle?') #asking for users input
side_a = input ()
print ('What is the length of the second side of the triangle?') #asking for users input
side_b = input ()
print ('What is the length of the third side of the triangle?') #asking for users input
side_c = input ()

if side_a == side_b == side_c:
    print ('The triangle is equilateral!')
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print ('The triangle is isoceles!')
else:
    print ('The triangle is scalene!')
