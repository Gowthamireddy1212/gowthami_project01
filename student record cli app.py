students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        students.append([name, roll])
        print("Student added!")

    elif choice == "2":
        print("\n--- Student Records ---")
        for s in students:
            print("Name:", s[0], "| Roll:", s[1])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
