monthly_salary = int(input("Enter Monthly Salary: "))
loan_amount = int(input("Enter Loan Amount: "))

if monthly_salary >= 30000 and loan_amount <= 10 * monthly_salary:
    print("You are eligible for the loan!")
    months = int(input("How many months do you want to repay the loan?: "))
    total_amount = loan_amount * 1.10 #10% interest
    monthly_payment = total_amount / months
    print(f"Total amount to repay (with interest): {total_amount:.2f}")
    print(f"Your monthly payment will be: {monthly_payment:.2f}")
else:
    if monthly_salary < 30000:
        print("Sorry, your salary is too low")
    if loan_amount > 10 * monthly_salary:
        print("Sorry, your loan is too high")   