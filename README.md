# Expense Budget App
## Overview
- This is a simple Python application to help users split bills and manage shared expenses with friends and family. 
- The application allows users to deposit, withdraw, track expenses, and split costs between multiple users.
- It uses classes to represent budgets and expenses.

## Features
- Create and manage budgets
- Deposit money into a budget
- Withdraw money from a budget
- Track expenses by category
- Split expenses between multiple users
- Display current balances and transaction history

## Getting Started
### Prerequisites
- Python 3.x
### Installation
1. Clone the repository or download the code files to your local machine.
   ```sh
   git clone https://github.com/your-username/expense-budget-app.git
   ```
2. Navigate to the project directory.
  -  cd expense-budget-app
### Usage
1. Run the main script to start the application.
  -  python budget_app.py
2. The script will execute and print the current balances, shared budget transactions, and expenses by category to the console.

### Code Structure
- `Budget` class: Represents a generic budget and contains methods for depositing, withdrawing, checking balance, and tracking transactions.
- `Expense` class: Inherits from Budget, including cost management methods by category.
- `User` class: Represents a user and manages their expenses.
- `split_expense` function: Splits an expense between multiple users.

### Main Function
- The `main` function demonstrates how to use the classes and functions to manage a shared expense budget between two users, Alice and Bob. 
- It includes examples of depositing money, adding expenses, splitting costs, and printing the results.

### Contributing
- Contributions are welcome! Please fork the repository and create a pull request with your changes.
