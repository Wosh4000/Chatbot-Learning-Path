import csv

def add_expense(expense, date, explanation, amount):
    with open('Expense Tracker/expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense, date, explanation, amount])
    print("Expense added successfully.")
    
    
def view_expenses():
    with open('Expense Tracker/expenses.csv', 'r', newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            
            
def main():
    try:
        with open('Expense Tracker/expenses.csv', 'r') as file:
            pass
    except FileNotFoundError:
        with open('Expense Tracker/expenses.csv', 'a', newline='') as file:
            headers = ['Expense', 'Date', 'Explanation', 'Amount']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            expense = input("Enter expense type: ")
            date = input("Enter date (YYYY-MM-DD): ")
            explanation = input("Enter explanation: ")
            amount = input("Enter amount: ")
            add_expense(expense, date, explanation, amount)
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
            
            
if __name__ == "__main__":
    main()
        
        