#Classes

class Customer:
  def __init__(self, name, balance= 0.0):
    self.name = name
    self.balance = balance
  #def __str__(self):
    #return self.name, self.balance
c1= Customer('Maria')
c2= Customer('Peter')

def deposit(self, amount):
  if amount < 0:
    print('you can not deposit a negative amount')
  self.balance += amount
  return self.name, self.balance

def withdraw(self, amount):
  self.balance -=amount
  if self.balance < 0:
    print('you can not overdraw your account')
  return self.name, self.balance

class Savings(Customer):
  def __init__(self, name, balance=0.0, savings=0.0):
    self.balance = balance
    self.name = name
    self.savings = savings
c1=Savings('Maria')
c2=Savings('Peter')


def transtosav(self, amount):
    if amount < 0:
      print('you can not transfer a negative amount')
    self.savings += amount
    self.balance -=amount
    if self.balance < 0:
      print('you can not overdraw your account')
    return self.name, self.balance, self.savings

def transtobal(self, amount):
    if amount < 0:
      print('you can not transfer a negative amount')
    self.balance += amount
    self.savings -= amount
    if self.savings < 0:
      print('you can not have negative savings')
    return self.name, self.balance, self.savings

deposit(c1, 100)
print(c1.balance)
transtosav(c1, 50)
print(c1.balance, c1.savings)

