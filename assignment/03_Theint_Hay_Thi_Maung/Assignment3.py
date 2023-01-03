'''Assignment 03

Python Basics III - Functions and Classes

This tutorial was written by Terry L. Ruas (University of Göttingen). The references for external contributors for which this material was anyhow adapted/inspired are in the Acknowledgments section (end of the document).
This notebook will cover the following tasks:
Dictionary
Classes
Task 01 – Dictionary
Imagine you have to write a (very simple) bookkeepingsystem for a bank that keeps track of the account balances of each of its customers.
Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers. For simplicity, assume customer names are unique identifier. (optional) Can you express that same functionality using a lambda function?
What are elegant ways to add or remove single and multiple customers using the functionality of dict?
Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account, etc.'''

from types import prepare_class


# function for replacing 0 balance where customers has no value in account
def span_dictionary(dist):
    for name in dist:
        print(name)
        if dist[name] == None and dist[name] == '':
            print(dist[name])
            dist[name] == 0
        else:
            print("No undefined customer balance")


# span_lamb = lambda name,dist: span_dictionary(name,dist)

# removing customers who has 0 balance in account.
def remove_multiple(dist):
    for key in dist:
        if dist[key] == 0:
            dist.pop(key)


# adding customers
def add_customer(name, amount, dist):
    if name in dist.keys():
        pass
    else:
        dist[name] = amount


# deposit balance in existing account
def deposit(name, amount, dist):
    if name in dist.keys():
        dist[name] = dist[name] + amount
    else:
        add_customer(name, amount, dist)


# withdraw balance from existing account
def withdraw(name, amount, dist):
    if name in dist.keys():
        if dist[name] != 0 and dist[name] > amount:
            dist[name] = dist[name] - amount
        else:
            print("Not enough credit")
    else:
        print("You are not a registered customer")


# Testing
dist = {'John': None, 'Iris': 100, "Belliyar": 50}
span_dictionary(dist)
print(dist)


'''Task 02 – Classes
The manager thinks that the simple bookkeeping system you have built is not powerful enough. She requests that you start from scratch and use classes instead.
Write a simple class with appropriate constructor __init__ that initializes an object of class Customer tracking the same information as in Task 01.
Now write two simple methods for class Customer that allow you to deposit and withdraw money for a given customer object.
Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account.
(Inheritance) Write a child class SavingsCustomer that inherits its features from the parent class Customer. 
A savings customer has an extra savings balance for receiving extra interest. The class should have a method to transfer money back and forth between the accounts' main balance as well as the savings balance. 
Do not forget to add reasonable error messages.'''


class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawing negative amounts")
        elif amount > self.balance:
            print("Overdrawing the account")
        else:
            self.balance = self.balance - amount
            print(self.balance)


class SavingsCustomer(Customer):
    def __init__(self, name, balance, saving=0):
        Customer.__init__(self, name, balance)
        self.saving = saving

    def mainbalance_to_saving(self, amount):
        if amount <= 0:
            print("Cannot transfer negative amount or 0")
        elif amount > self.balance:
            print("Over credits")
        else:
            self.balance = self.balance - amount
            self.saving = self.saving + amount
            print("balance:" + str(self.balance) + "saving:" + str(self.saving))

    def saving_to_mainbalance(self, amount):
        if amount <= 0:
            print("Cannot transfer negative amount or 0")
        elif amount > self.saving:
            print("Over credits")
        else:
            self.saving = self.saving - amount
            self.balance = self.balance + amount
            print("balance:" + str(self.balance) + "saving:" + str(self.saving))


# Testing
'''customer = Customer("Iris", 100)
customer.deposit(10)
customer.withdraw(90)'''

sav_customer = SavingsCustomer("May", 80)
sav_customer.mainbalance_to_saving(50)
