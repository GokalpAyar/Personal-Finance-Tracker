class Transaction:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, description, amount, category):
        transaction = Transaction(description, amount, category)
        self.transactions.append(transaction)

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("\nTransactions:")
            for transaction in self.transactions:
                print(f"{transaction.description} - ${transaction.amount} ({transaction.category})")

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

    def view_balance(self):
        balance = self.calculate_balance()
        print(f"\nCurrent Balance: ${balance:.2f}")

    def view_expense_report(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction.amount < 0:
                category = transaction.category
                if category in expense_categories:
                    expense_categories[category] += transaction.amount
                else:
                    expense_categories[category] = transaction.amount

        if not expense_categories:
            print("\nNo expense transactions recorded.")
        else:
            print("\nExpense Report:")
            for category, total_expense in expense_categories.items():
                print(f"{category}: ${-total_expense:.2f}")


def main():
    finance_tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Current Balance")
        print("4. View Expense Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter transaction description: ")
            amount = float(input("Enter transaction amount: "))
            category = input("Enter transaction category: ")
            finance_tracker.add_transaction(description, amount, category)
            print("Transaction recorded.")

        elif choice == "2":
            finance_tracker.view_transactions()

        elif choice == "3":
            finance_tracker.view_balance()

        elif choice == "4":
            finance_tracker.view_expense_report()

        elif choice == "5":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()


