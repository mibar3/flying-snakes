print('Type in any string:')
string=input()
string=string.replace(' ', '')
list_string = list(string)
dic_string = {}
for element in list_string:
  if element in dic_string:
    dic_string[element] += 1
  else:
    dic_string[element] = 1

print(dic_string)
