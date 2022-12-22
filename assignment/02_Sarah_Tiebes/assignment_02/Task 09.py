
import math
def tay_ser(x,n):
  e_app = 0
  for i in range(n):
    e_app += x**i/math.factorial(i)
  return e_app

def pre_e(x, threshold):
  n=1
  e_app=tay_ser(x,n)
  next_value= abs(math.exp(x) - e_app)
  while next_value > threshold:
    n+=1
    e_app = tay_ser(x,n)
    next_value = abs(math.exp(x)- e_app)
    if next_value < threshold:
      print(e_app)
pre_e(2, 5)
