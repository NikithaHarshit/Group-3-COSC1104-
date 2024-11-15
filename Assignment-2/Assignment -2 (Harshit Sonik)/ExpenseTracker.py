def display_menu():
    """
    Display options for the expense tracker.
    """
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. Exit")

def add_expense(expenses):
    """
    Add a new expense to the list.
    """
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter expense amount: $"))
        expenses.append({"description": description, "amount": amount})
        print(f"Added: {description} - ${amount:.2f}")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def view_total_expenses(expenses):
    """
    Calculate and display the total expenses.
    """
    if not expenses:
        print("\nNo expenses recorded.")
    else:
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Expenses: ${total:.2f}")
        print("Expense Details:")
        for expense in expenses:
            print(f"- {expense['description']}: ${expense['amount']:.2f}")

def main():
    """
    Main function to manage expenses.
    """
    expenses = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-3): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_total_expenses(expenses)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
