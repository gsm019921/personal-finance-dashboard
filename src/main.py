monthly_income = float(input("Enter your monthly income: "))
rent = float(input("Enter your rent: "))
food = float(input("Enter your food expenses: "))
gas = float(input("Enter your gas expenses: "))
insurance = float(input("Enter your insurance expenses: "))
subscriptions = float(input("Enter your subscriptions expenses: "))
entertainment = float(input("Enter your entertainment expenses: "))
savings_goal = float(input("Enter your savings goal: "))
budget_limit = float(input("Enter your budget limit: "))


expenses = [rent, food, gas, insurance, subscriptions, entertainment]
expense_names = ["Rent", "Food", "Gas", "Insurance", "Subscriptions", "Entertainment"]

total_expenses = sum(expenses)
money_left = monthly_income - total_expenses
amount_after_savings = money_left - savings_goal
savings_rate = (savings_goal / monthly_income) * 100
expense_rate = (total_expenses / monthly_income) * 100

def print_expense_breakdown():
    print("\nExpense Breakdown:")

    for name, amount in zip(expense_names, expenses):
        print(f"{name}: ${amount:,.2f}")    

def print_summary():
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Money Left: ${money_left:,.2f}")
    print(f"Savings Goal: ${savings_goal:,.2f}")
    print(f"Savings Rate: {savings_rate:,.2f}%")
    print(f"Money Left After Savings: ${amount_after_savings:,.2f}")
    print(f"Expense Rate: {expense_rate:,.2f}%")

def check_budget_status():
    if total_expenses < budget_limit:
        print("You are under budget.")
    elif total_expenses == budget_limit:
        print("You hit your budget exactly.")
    else: 
        print("You are over budget.")

    if amount_after_savings > 0:
        print("Good job! You still have money left after savings.")
    elif amount_after_savings == 0: 
        print("You used your full budget exactly.")
    else: 
        print("Warning: your savings goal may be too high.")

print(f"Monthly Income: ${monthly_income:,.2f}")
print_expense_breakdown()
print_summary()
check_budget_status()




