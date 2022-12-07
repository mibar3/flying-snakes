MathExp = input(print('Put in a mathematical expression which contains diffrent brackets'))
open_list = ['(','[','{']
close_list = [')',']','}']            #list of the possible brackets
def check(MathExp):
  Ablage = []
  for char in MathExp:
    if char in open_list:
      Ablage.append(char)             #store of the opening brackets
    elif char in close_list:
      pos=close_list.index(char)      #if it finds a closing brackets: store the typ of the closing brackets: index in the close_list shows the typ
      if ((len(Ablage) > 0) and ((open_list[pos]) == Ablage[-1])):
          Ablage.pop()
      else:
          print('incorrect Input')
  if len(Ablage) == 0:
    print('correct Input')              #only if list is empty, every opening bracket found a closing bracket = correct input
  else: print('incorrect Input')
check(MathExp)
