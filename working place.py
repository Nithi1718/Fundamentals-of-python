class BankAccount:

    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance: ₹", self.balance)

    # This method will be overridden
    def calculate(self):
        print("No calculation available.")


# Inheritance
class SavingsAccount(BankAccount):

    def calculate(self):
        interest = self.balance * 0.04
        print("Account Type: Savings Account")
        print("Interest: ₹", interest)


# Inheritance
class CurrentAccount(BankAccount):

    def calculate(self):
        charge = 500
        print("Account Type: Current Account")
        print("Service Charge: ₹", charge)


# List to store accounts
accounts = []


while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Account Details")
    print("7. Calculate")
    print("8. Display All Accounts")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # Create Savings Account
    if choice == "1":

        account_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))

        account = SavingsAccount(
            account_number,
            customer_name,
            balance
        )

        accounts.append(account)

        print("Savings Account created successfully.")


    # Create Current Account
    elif choice == "2":

        account_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))

        account = CurrentAccount(
            account_number,
            customer_name,
            balance
        )

        accounts.append(account)

        print("Current Account created successfully.")


    # Deposit
    elif choice == "3":

        account_number = input("Enter account number: ")

        found = False

        for account in accounts:

            if account.account_number == account_number:

                amount = float(input("Enter deposit amount: "))

                account.deposit(amount)

                found = True
                break

        if not found:
            print("Account not found.")


    # Withdraw
    elif choice == "4":

        account_number = input("Enter account number: ")

        found = False

        for account in accounts:

            if account.account_number == account_number:

                amount = float(input("Enter withdrawal amount: "))

                account.withdraw(amount)

                found = True
                break

        if not found:
            print("Account not found.")


    # Check Balance
    elif choice == "5":

        account_number = input("Enter account number: ")

        found = False

        for account in accounts:

            if account.account_number == account_number:

                account.display_balance()

                found = True
                break

        if not found:
            print("Account not found.")


    # Account Details
    elif choice == "6":

        account_number = input("Enter account number: ")

        found = False

        for account in accounts:

            if account.account_number == account_number:

                account.display_details()

                if isinstance(account, SavingsAccount):
                    print("Account Type: Savings Account")

                elif isinstance(account, CurrentAccount):
                    print("Account Type: Current Account")

                found = True
                break

        if not found:
            print("Account not found.")


    # Polymorphism
    elif choice == "7":

        account_number = input("Enter account number: ")

        found = False

        for account in accounts:

            if account.account_number == account_number:

                account.calculate()

                found = True
                break

        if not found:
            print("Account not found.")


    # Display all accounts
    elif choice == "8":

        if len(accounts) == 0:

            print("No accounts available.")

        else:

            print("\n===== ALL ACCOUNTS =====")

            for account in accounts:

                print(
                    account.account_number,
                    "-",
                    account.customer_name,
                    "- ₹",
                    account.balance
                )


    # Exit
    elif choice == "9":

        print("Thank you for using Bank Management System.")
        break


    else:

        print("Invalid choice. Please try again.")