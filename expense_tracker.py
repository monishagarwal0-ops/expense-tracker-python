expenses = []

def add_expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("\nExpense Added Successfully!\n")


def view_expenses():

    if len(expenses) == 0:
        print("\nNo Expenses Found!\n")
        return

    print("\nExpense List:")

    for expense in expenses:
        print(
            f"Category: {expense['category']} | "
            f"Amount: ₹{expense['amount']}"
        )

    print()


def total_expense():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total}\n")


def highest_expense():

    if len(expenses) == 0:
        print("\nNo Expenses Found!\n")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\nHighest Expense:")
    print(
        f"Category: {highest['category']} | "
        f"Amount: ₹{highest['amount']}"
    )


def delete_expense():

    category = input("Enter Category to Delete: ")

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            expenses.remove(expense)

            print("\nExpense Deleted Successfully!\n")
            return

    print("\nExpense Not Found!\n")


while True:

    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Highest Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        highest_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")