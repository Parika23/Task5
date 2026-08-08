# ATM Simulation System

## Project Description

The **ATM Simulation System** is a menu-driven Python mini project developed using **Object-Oriented Programming (OOP)**. The application simulates basic ATM operations such as creating an account, logging in, checking balance, depositing money, withdrawing money, and changing the PIN.

The project demonstrates the fundamental Python concepts covered in Week 1, including variables, conditional statements, loops, functions, data structures, exception handling, OOP, and file handling.

## Features

* Create a new bank account
* Login using account number and PIN
* Check account balance
* Deposit money
* Withdraw money
* Change PIN
* Store account information in a CSV file
* Handle invalid user input using exception handling
* Menu-driven interface

## Technologies Used

* Python
* Object-Oriented Programming
* CSV File Handling

## Python Concepts Demonstrated

### 1. Variables

Variables are used to store account details such as account number, name, PIN, balance, and transaction amounts.

### 2. Conditional Statements

`if`, `elif`, and `else` statements are used for:

* Menu selection
* Login validation
* Balance validation
* Deposit and withdrawal validation
* PIN validation

### 3. Loops

`while` loops are used to repeatedly display the menus and allow the user to perform multiple operations.

### 4. Functions and Methods

Functions and class methods are used to organize the program into smaller and reusable sections.

### 5. Data Structures

* **Dictionary:** Stores account objects using account numbers as keys.
* **Set:** Stores unique account numbers.
* **Tuple:** Stores the fixed menu options.

### 6. Object-Oriented Programming

The project uses two classes:

#### BankAccount

Represents a bank account.

Methods include:

* `check_balance()`
* `deposit()`
* `withdraw()`
* `change_pin()`

#### ATM

Controls the ATM system.

Methods include:

* `load_accounts()`
* `save_accounts()`
* `create_account()`
* `login()`
* `account_menu()`
* `main_menu()`

### 7. Constructor

The `__init__()` method is used to initialize objects with their required attributes.

### 8. Exception Handling

`try-except` blocks are used to handle invalid numerical input and file-related errors without crashing the program.

### 9. File Handling

Account information is stored permanently in an `accounts.csv` file. The program reads the data when it starts and updates the file whenever account information changes.

## Project Structure

```text
Task5/
│
├── atm.py
├── accounts.csv
└── README.md
```

The `accounts.csv` file is automatically created when the first account is created.

## How to Run

1. Make sure Python is installed on your computer.
2. Save the program as `atm.py`.
3. Open the terminal in the project folder.
4. Run:

```bash
python atm.py
```

5. Select an option from the menu.

## Sample Menu

```text
============================
       ATM SIMULATION
============================
1. Create Account
2. Login
3. Exit
```

After logging in:

```text
----- ACCOUNT MENU -----
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Logout
```

## Conclusion

This project demonstrates how Python's basic programming concepts can be combined with Object-Oriented Programming to create a simple, structured, and functional ATM simulation system. It also demonstrates persistent data storage using CSV file handling and graceful handling of invalid user input.
