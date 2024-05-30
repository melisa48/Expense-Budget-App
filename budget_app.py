import json
from datetime import datetime

class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, note=""):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.transactions.append({
            'amount': amount,
            'note': note,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp
        })

    def withdraw(self, amount, note=""):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.check_funds(amount):
            self.balance -= amount
            self.transactions.append({
                'amount': -amount,
                'note': note,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp
            })
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def get_transactions(self):
        return self.transactions


class Expense(Budget):
    def __init__(self, name, budget, balance=0):
        super().__init__(name, balance)
        self.budget = budget
        self.expenses = {}

    def add_expense(self, category, amount, note=""):
        if category not in self.expenses:
            self.expenses[category] = Budget(category, 0)
        self.withdraw(amount, note)
        self.expenses[category].deposit(amount, note)

    def get_budget(self):
        return self.budget

    def get_balance_left(self):
        return self.budget - self.balance

    def get_expenses_by_category(self, category):
        if category in self.expenses:
            return self.expenses[category].get_transactions()
        return []

    def get_all_expenses(self):
        all_expenses = {}
        for category, budget in self.expenses.items():
            all_expenses[category] = budget.get_transactions()
        return all_expenses


class User:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.get_balance() for expense in self.expenses)


def split_expense(users, amount, note=""):
    split_amount = amount / len(users)
    for user in users:
        user.expenses[0].withdraw(split_amount, note)  # Assuming a single shared expense budget per user

def main():
    # create users
    alice = User("Alice")
    bob = User("Bob")

    # create a shared expense budget
    shared_expense_budget = Expense("Shared Expense", 1000)

    # add shared expense budget to users
    alice.add_expense(shared_expense_budget)
    bob.add_expense(shared_expense_budget)

    # deposit money into the shared expense budget
    shared_expense_budget.deposit(200, "Initial Deposit")

    # withdraw money from the shared expense budget
    shared_expense_budget.add_expense("Groceries", 100, "Grocery shopping")

    # split an expense between users
    split_expense([alice, bob], 50, "Dinner")

    # print the balances
    print(f"Alice's balance: {alice.expenses[0].get_balance()}")
    print(f"Bob's balance: {bob.expenses[0].get_balance()}")

    # print the shared budget transactions
    print("Shared Budget Transactions:")
    for transaction in shared_expense_budget.get_transactions():
        print(f"  Amount: {transaction['amount']}, Note: {transaction['note']}, Timestamp: {transaction['timestamp']}")

    # print expenses by category
    print("\nExpenses by Category:")
    for category, transactions in shared_expense_budget.get_all_expenses().items():
        print(f"  {category}:")
        for transaction in transactions:
            print(f"    Amount: {transaction['amount']}, Note: {transaction['note']}, Timestamp: {transaction['timestamp']}")

if __name__ == '__main__':
    main()
