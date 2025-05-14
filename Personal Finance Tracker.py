print("PERSONAL FINANCE TRACKER")
print("Welcome")

savings = 0
expenses = 0

def add_income():
    global savings
    print("Income Sources: Salary, Freelancing, Investment, Gifts, Other")
    try:
        amt = int(input("Enter Income Amount: "))
        if amt <= 0:
            print("Enter a valid/positive amount.")
        else:
            savings += amt
            print(f"Income added. Total Savings: {savings}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_expense():
    global savings, expenses
    print("Expense Categories: Rent, Utilities, Food, Transportation, Entertainment")
    try:
        amt1 = float(input("Enter Expense Amount: "))
        if amt1 <= 0:
            print("Enter a valid/positive amount.")
        else:
            expenses += amt1
            savings -= amt1
            print(f"Expense added. Remaining Savings: {savings}")
    except ValueError:
        print("Invalid input. Please enter an amount.")

def view_savings():
    if savings == 0 and expenses == 0:
        print("No income or expense data available.")
    else:
        print(f"Savings: {savings}")

def view_expenses():
    print(f"Total Expenses: {expenses}")

def save_data():
    try:
        with open("User_Data.txt", mode='w') as file:
            file.write(f'Your Savings: ${savings}\n')
            file.write(f'Your Expenses: ${expenses}\n')
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data():
    global savings, expenses
    try:
        with open("User_Data.txt", mode='r') as file:
            contents = file.readlines()
            for content in contents:
                print(content)
            print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")

while True:
    print("""
        Main Menu
        1. Add Income
        2. Add Expenses
        3. View Savings
        4. View Expenses
        5. Save Data
        6. Load Data
        7. Exit
    """)

    try:
        choice = int(input("Choose your preferred menu: "))
    except ValueError:
        print("Invalid choice. Enter a number from 1 to 7.")
        continue

    if choice == 1:
        add_income()
    elif choice == 2:
        add_expense()
    elif choice == 3:
        view_savings()
    elif choice == 4:
        view_expenses()
    elif choice == 5:
        save_data()
    elif choice == 6:
        load_data()
    elif choice == 7:
        print("Goodbye!")
        break
    else:
        print("Enter a valid option from the menu.")