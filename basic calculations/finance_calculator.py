monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")
monthly_savings = int(monthly_income) - int(monthly_expenses)
projected_savings = int(monthly_savings) * 12 + int(monthly_savings) * 12 * 0.05

print("Your monthly savings is:$",monthly_savings)
print("Projected savings after one year, with interest, is:$",projected_savings)
