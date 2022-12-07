print('Please, give me a mathematical expression which contains brackets')
MathExp= input()
openBracets=['(']
closeBracets=[')']
Ablage_open = []
Ablage_close = []
for char in MathExp:
  if char in openBracets:
    Ablage_open.append(char)
  elif char in closeBracets:
    Ablage_close.append(char)

if len(Ablage_open) == len(Ablage_close):
    print('correct Input')
elif len(Ablage_open) != len(Ablage_close):
    print('incorrect Input')
