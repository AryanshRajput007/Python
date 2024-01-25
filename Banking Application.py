import random


class Bank:

  def __init__(self, Name):
    self.Name = Name
    self.customers = []

  def add_customers(self, customer):
    self.customers.append(customer)

  @staticmethod
  def account_number_generator():
    return ''.join(random.choice('0123456789') for _ in range(12))

  @staticmethod
  def pin_generator():
    return ''.join(random.choice('0123456789') for _ in range(4))


class Account:

  def __init__(self, customer):
    self.customer = customer

  def account_checker(self, account_number, pin):
    return self.customer.account.get(
      'Account Number') == account_number and self.customer.account.get(
        'Pin') == pin

  def check_balance(self):
    return self.customer.check_balance()

  def print_account_details(self):
    print("Account Details:")
    print("Name:", self.customer.account.get('Name'))
    print("Account Number:", self.customer.account.get('Account Number'))
    print("Pin:", self.customer.account.get('Pin'))
    print("Balance:", self.customer.check_balance())


class Customer:

  def __init__(self, Name, Balance):
    self.name = Name
    self.account_Number = Bank.account_number_generator()
    self.pin = Bank.pin_generator()
    self.Balance = Balance
    self.account = {}
    self.account_creator()

  def account_creator(self):
    self.account = {
      'Name': self.name,
      'Account Number': self.account_Number,
      'Pin': self.pin,
      'Balance': self.Balance
    }

  def deposit(self, amount):
    self.Balance += amount

  def withdraw(self, amount):
    if self.Balance >= amount:
      self.Balance -= amount
      return True
    else:
      return False

  def check_balance(self):
    return self.Balance


# Function to create n customer accounts
def create_customer_accounts(n):
  customers = []
  for _ in range(n):
    name = input("Enter customer name: ")
    initial_balance = float(
      input("Enter initial balance for {}: ".format(name)))
    customers.append(Customer(name, initial_balance))
  return customers


# Function for user menu
def user_menu(account):
  while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Print Account Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      amount = float(input("Enter the deposit amount: "))
      account.customer.deposit(amount)
      print("Deposit successful. Updated balance:", account.check_balance())
    elif choice == '2':
      amount = float(input("Enter the withdrawal amount: "))
      withdraw_result = account.customer.withdraw(amount)
      if withdraw_result:
        print("Withdrawal successful. Updated balance:",
              account.check_balance())
      else:
        print("Insufficient balance for withdrawal.")
    elif choice == '3':
      print("Current balance:", account.check_balance())
    elif choice == '4':
      account.print_account_details()
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")


# Example usage with n customers
number_of_customers = int(input("Enter the number of customers: "))
customer_accounts = create_customer_accounts(number_of_customers)

# Perform operations for each customer
for customer in customer_accounts:
  account = Account(customer)
  print("\nOperations for", customer.name)
  user_menu(account)
