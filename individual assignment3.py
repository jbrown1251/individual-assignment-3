# Problem 1
# Simple calculator for +, -, *, /

# Prompt user for inputs
num1 = float(input("Enter the num1: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the num2: "))

# Perform operation with validation
if operator == "+":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed.")
else:
    print("\nInvalid operator entered. Please use +, -, *, or /.")

# =========================================
# Problem 2
# Track progress toward sales target over 5 days

# Prompt for sales target
sales_target = float(input("\nEnter total sales target: "))

# Variable to keep track of total sales
total_sales = 0.0

# Loop for 5 days
for day in range(1, 6):
    daily_sales = float(input(f"Enter day {day} sales: "))
    total_sales += daily_sales  # add to cumulative total
    percentage = (total_sales / sales_target) * 100
    print(f"Cumulative sales: {total_sales:.1f} ({percentage:.1f} %)")