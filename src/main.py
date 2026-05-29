import csv

project_name = "Personal Finance Dashboard"
income = float(input("Enter your income: "))
expense_categories = {
    "Rent": 700,
    "Groceries": 85.43,
    "Gas": 42.10,
    "Restaurant": 28.75
}

expenses = expense_categories.values()
total_expenses = sum(expenses)

largest_expense_category = ""
largest_expense = 0

for category, amount in expense_categories.items():
    if amount > largest_expense:
        largest_expense = amount
        largest_expense_category = category

savings = income - total_expenses
savings_rate = savings / income
savings_rate_percent = savings_rate * 100

print(f"Project: {project_name}")
print(f"Income: ${income:,.2f}")
print(f"Expenses: ${total_expenses:,.2f}")
print("Spending by Category:")

for category, amount in expense_categories.items():
    print(f"{category}: ${amount:,.2f}")

print(f"Largest Expense: {largest_expense_category} - ${largest_expense:,.2f}")
print(f"Savings: ${savings:,.2f}")
print(f"Savings Rate: {savings_rate_percent:,.2f}%")

if savings_rate_percent >= 30:
    print("Excellent savings rate.")
elif savings_rate_percent >= 20:
    print("Good savings rate.")
else: 
    print("Try to increase your savings rate.")

print()
print("Reading transactions from CSV:")
print("------------------------------")

with open("data/transactions.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


