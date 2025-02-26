#class BankAccount:
 #   def __init__(self, owner, balance=0):
  #      self.owner = owner
   #     self.balance = balance
#
 #   def deposit(self, amount):
  #      if amount > 0:
   #         self.balance += amount
    #        return True
     #   return False

   # def withdraw(self, amount):
    #    if 0 < amount <= self.balance:
     #       self.balance -= amount
      #      return True
       # return False

   # def get_balance(self):
    #    return self.balance
#account = BankAccount("Alice", 100)
#account.deposit(50)
#account.withdraw(30)
#print(account.get_balance())

# Chatgpt convo link
# https://chatgpt.com/c/67beb93c-5858-8010-ac12-d1ee7fcf1114

# Code with documentation:
class BankAccount:
    """
    A class representing a simple bank account.

    Attributes:
        owner (str): The name of the account owner.
        balance (float): The current balance of the account.
    """

    def __init__(self, owner, balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            owner (str): The name of the account owner.
            balance (float, optional): The initial balance of the account. Defaults to 0.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be greater than zero.

        Returns:
            bool: True if deposit is successful, False otherwise.
        """
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be greater than zero and not exceed the available balance.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        """
        Retrieves the current balance of the account.

        Returns:
            float: The current account balance.
        """
        return self.balance

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())