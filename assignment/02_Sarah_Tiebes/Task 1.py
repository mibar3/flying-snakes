#Dictionary

def buildDatabase(*costumers):
  costumers = [*costumers]
  balance = [0] * len(costumers)
  Database_1 = zip(costumers, balance)
  Database = dict(Database_1)
  return Database
Database = buildDatabase('Maria', 'Peter')

def add_remCostumers():
  inputlist= input(print('if you want to add a costumer typ add \n if you want to remove a costumer typ remove'))
  if inputlist == 'add':
    add_costumer = input(print('Who do you want to add?:'))
    balance = 0
    Database.update({add_costumer: balance})
    print(Database)
  else:
    input(print('Who do you want to remove?:'))
    del Database[input()]


def deposit(costumer):
  dep_money= float(input(print('how much do you want to deposit?:')))
  if dep_money < 0:
    return'You can not deposit negative amount'
  Database[costumer] += dep_money

  return Database


def withdraw(costumer):
  with_money= float(input('how much do yoou want to withdraw?:'))
  Database[costumer] -= with_money
  if balance < 0:
    return('you can not overdraw your account')
  return Database

