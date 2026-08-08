import csv
import os


class BankAccount:
    def __init__(self, account_no, name, pin, balance=0.0):
        self.account_no = account_no
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return False

        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Updated Balance: ₹{self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("Insufficient balance.")
            return False

        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Updated Balance: ₹{self.balance:.2f}")
        return True

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("Incorrect current PIN.")
            return False

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits.")
            return False

        self.pin = new_pin
        print("PIN changed successfully.")
        return True


class ATM:
    FILE_NAME = "accounts.csv"

    def __init__(self):
        self.accounts = {}
        self.account_numbers = set()
        self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    account_no = row["Account No"]
                    name = row["Name"]
                    pin = row["PIN"]
                    balance = float(row["Balance"])

                    account = BankAccount(
                        account_no,
                        name,
                        pin,
                        balance
                    )

                    self.accounts[account_no] = account
                    self.account_numbers.add(account_no)

        except (ValueError, KeyError):
            print("Error while reading account data.")

    def save_accounts(self):
        try:
            with open(self.FILE_NAME, "w", newline="") as file:
                fieldnames = ["Account No", "Name", "PIN", "Balance"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

                for account in self.accounts.values():
                    writer.writerow({
                        "Account No": account.account_no,
                        "Name": account.name,
                        "PIN": account.pin,
                        "Balance": account.balance
                    })

        except IOError:
            print("Error while saving account data.")

    def create_account(self):
        print("\n----- CREATE ACCOUNT -----")

        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        while True:
            account_no = input("Enter account number: ").strip()

            if not account_no.isdigit():
                print("Account number must contain only digits.")
                continue

            if account_no in self.account_numbers:
                print("Account number already exists.")
                continue

            break

        while True:
            pin = input("Create a 4-digit PIN: ").strip()

            if len(pin) == 4 and pin.isdigit():
                break

            print("PIN must be exactly 4 digits.")

        while True:
            try:
                balance = float(input("Enter initial deposit: "))

                if balance < 0:
                    print("Initial deposit cannot be negative.")
                else:
                    break

            except ValueError:
                print("Please enter a valid amount.")

        account = BankAccount(account_no, name, pin, balance)

        self.accounts[account_no] = account
        self.account_numbers.add(account_no)

        self.save_accounts()

        print("\nAccount created successfully!")
        print(f"Account Number: {account_no}")

    def login(self):
        print("\n----- LOGIN -----")

        account_no = input("Enter account number: ").strip()

        if account_no not in self.accounts:
            print("Account not found.")
            return

        account = self.accounts[account_no]

        attempts = 3

        while attempts > 0:
            pin = input("Enter PIN: ").strip()

            if pin == account.pin:
                print(f"\nWelcome, {account.name}!")
                self.account_menu(account)
                return

            attempts -= 1

            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempt(s) remaining.")
            else:
                print("Too many incorrect attempts.")

    def account_menu(self, account):
        menu_options = (
            "Check Balance",
            "Deposit Money",
            "Withdraw Money",
            "Change PIN",
            "Logout"
        )

        while True:
            print("\n----- ACCOUNT MENU -----")

            for index, option in enumerate(menu_options, start=1):
                print(f"{index}. {option}")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                account.check_balance()

            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        self.save_accounts()
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        self.save_accounts()
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == "4":
                old_pin = input("Enter current PIN: ").strip()
                new_pin = input("Enter new PIN: ").strip()

                if account.change_pin(old_pin, new_pin):
                    self.save_accounts()

            elif choice == "5":
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    def main_menu(self):
        main_options = (
            "Create Account",
            "Login",
            "Exit"
        )

        while True:
            print("\n============================")
            print("       ATM SIMULATION")
            print("============================")

            for index, option in enumerate(main_options, start=1):
                print(f"{index}. {option}")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("\nThank you for using the ATM.")
                break

            else:
                print("Invalid choice. Please select 1, 2, or 3.")


def main():
    atm = ATM()
    atm.main_menu()


if __name__ == "__main__":
    main()