#!/usr/bin/env python
# coding: utf-8

# In[3]:


# long-termgoal = The customer must pass authentication before withdrawing money / Authentication is performed by checking a PIN / 
# The PIN can be correct or not / Unsuccessful attempts are counted / If the counter exceeds a limit, then the customer is rejected

# Goal for this code = The customer must pass authentication before withdrawing money / Authentication is performed by checking a PIN / 
# The PIN can be correct or not

import random
import time


class Accounts:
    # Defining Account instance variables.
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance


    # class function to calculate difference between the balance and the amount withdrawn.
    def withdraw(self, amount):
        self.balance -= amount

    # class function to calculate the sum between the balance and the amount deposited.
    def deposit(self, amount):
        self.balance += amount


# Revieves pin from user input and validates input.
def getAccountPin(times = 3):
    while True:
        times -= 1
        pin = input("\nEnter four digit account pin: ")
        try:
            pin = int(pin)
            if pin == 1234:
                return pin
            elif times > 0:
                print(f"\n{pin} is not a valid pin. You have {times} chances left")
            else:
                print("Too many wrong attempts. Your request was rejected. Please take your card!")
        except ValueError:
            print(f"\n{pin} is not a vaild pin... Try again")


# Recieves user input for option selection and validates selection.
def getSelection():
    while True:
        selection = input("\nEnter your selection: ")
        try:
            selection = int(selection)
            if selection >= 1 and selection <= 4:
                return selection
            else:
                print(f"{selection} is not a valid choice... Try again")
        except ValueError:
            print(f"{selection} is not a valid choice... Try again")


# Returns the current working accounts balance.
def viewBalance(workingAccount):
    return workingAccount.balance


# Recieves user input and validates if input is either yes, y, no, or n.
def correctAmount(amount):
    while True:
        answer = input(f"Is ${amount} the correct amount, Yes or No? ")
        try:
            answer = answer.lower()
            if answer == "y" or answer == "yes":
                return True
            elif answer == "n" or answer == "no":
                return False
            else:
                print("Please enter a valid response")
        except AttributeError:
            print("Please enter a valid response")


# Recieves user input on amount to withdraw and validates inputed value.
def withdraw(workingAccount):
    while True:
        try:
            amount = float(input("\nEnter amount you want to withdraw: "))
            try:
                amount = round(amount, 2)
                if amount > 0 and ((workingAccount.balance) - amount) > 0:
                    answer = correctAmount(amount)
                    if answer == True:
                        print("Verifying withdraw")
                        time.sleep(random.randint(1, 2))
                        return amount
                elif (((workingAccount.balance) - amount) < 0):
                    print("\nYour balance is less than the withdraw amount")
                elif amount == 0:
                    answer = correctAmount(amount)
                    if answer == True:
                        print("Canceling withdraw")
                        time.sleep(random.randint(1, 2))
                        return amount
                else:
                    print("\nPlease enter an amount greater than or equal to 0")
            except TypeError:
                print("\nAmount entered is invalid... Try again")
        except ValueError:
            print("\nAmount entered is invalid... Try again")


# Recieves user input on amount to deposit and validates inputed value.
def deposit(workingAccount):
    while True:
        try:
            amount = float(input("\nEnter amount you want to deposit: "))
            try:
                amount = round(amount, 2)
                if amount > 0:
                    answer = correctAmount(amount)
                    if answer == True:
                        print("Verifying deposit")
                        time.sleep(random.randint(1, 2))
                        return amount
                elif amount == 0:
                    answer = correctAmount(amount)
                    if answer == True:
                        print("Canceling deposit")
                        time.sleep(random.randint(1, 2))
                        return amount
                else:
                    print("\nPlease enter an amount greater than or equal to 0")
            except TypeError:
                print("\nAmount entered is invalid... Try again")
        except ValueError:
            print("\nAmount entered is invalid... Try again")


# End of program to print out account information and return false to end main loop
def exitATM(workingAccount):
    print("\nTransaction is now complete.")
    print("Transaction number: ", random.randint(10000, 1000000))
    print("Thanks for using this ATM")
    return False


def main():
    # Creating all accounts possible, could be stored or read from a file/database instead for better functionality overall.
    accounts = []
    for i in range(1000, 9999):
        account = Accounts(i, 0)
        accounts.append(account)

    # ATM Processes loop
    loop = True
    while loop == True:
        pin = getAccountPin()
        print(pin)
        # Account session loop
        while loop == True:
            # Menu Selection
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

            selection = getSelection()

            # Getting working account object by comparing pins
            for acc in accounts:
                # Comparing user inputted pin to pins created
                if acc.pin == pin:
                    workingAccount = acc
                    break

            # View Balance
            if selection == 1:
                print(f"\nYour balance is ${viewBalance(workingAccount)}")
            # Withdraw
            elif selection == 2:
                workingAccount.withdraw(withdraw(workingAccount))
                print(f"\nUpdated Balance: ${workingAccount.balance}")
            # Deposit
            elif selection == 3:
                workingAccount.deposit(deposit(workingAccount))
                print(f"\nUpdated Balance: ${workingAccount.balance}")
            # Exit
            elif selection == 4:
                loop = exitATM(workingAccount)
            # Invalid input
            else:
                print("Enter a valid choice")


if __name__ == "__main__":
    main()


# 
