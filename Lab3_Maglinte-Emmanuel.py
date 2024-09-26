monthly_salary = int(input("Enter Amount of Monthly Salary: "))
loan_amount = int(input("Enter Loan Amount: "))
valid_loan = monthly_salary * 10
months = int(input("How many Months of payment: "))

if monthly_salary <= 30000 and loan_amount >= valid_loan:
    print(months)
    payment_to_loan = loan_amount * 0.10
    print("Amount to Pay: ",payment_to_loan)
    print("Months to Pay: ", months)
else:
    print("Loan Declined")

