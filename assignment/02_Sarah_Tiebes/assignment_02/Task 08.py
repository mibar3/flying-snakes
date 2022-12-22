def unlim_pow(x, n):
  if n == 0:
    return 1
  else:
    return x * unlim_pow(x, n-1)
print(unlim_pow(3, 7))
