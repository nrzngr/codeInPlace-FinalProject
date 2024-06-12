import datetime


expenses = []


def add_expense():
    """
    Adds a new expense to the expenses list.

    Prompts the user to enter the date, category, amount, and description of the expense.
    Validates the input and adds the expense to the expenses list.

    Parameters:
    None

    Returns:
    None
    """
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

    category = input("Enter Category")
    while True:
        amount = input("Enter amount: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be a positive number")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number")

    description = input("Enter description (optional): ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded")
    else:
        print("Expenses: ")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Amount: {
                  expense['amount']:.2f}, Description: {expense['description']}")


def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: {total:.2f}")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Calculate total")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
