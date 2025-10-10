from datetime import datetime

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = datetime.now().strftime("%Y-%m-%d")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        expenses.append([date, category, amount])
        print("Expense added!")

    elif choice == "2":
        if not expenses:
            print("No expenses yet!")
        else:
            total = 0
            print("\nDate        Category     Amount")
            print("------------------------------")
            for e in expenses:
                print(f"{e[0]}   {e[1]}   ₹{e[2]}")
                total += e[2]
            print("------------------------------")
            print("Total =", total)

    elif choice == "3":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, try again!")