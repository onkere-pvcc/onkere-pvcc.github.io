# Name: Omwira Nkere
# Prog Purpose: find the pay for every position

import datetime

# Define job category codes and pay rates
pay_rates = {
    'C': ('Cashier', 16.50),
    'S': ('Stocker', 15.75),
    'J': ('Janitor', 15.75),
    'M': ('Maintenance', 19.50)
}

deductions = {
    'Federal Income Tax': 0.12,
    'State Income Tax': 0.03,
    'Social Security Tax': 0.062,
    'Medicare Tax': 0.0145
}

def main():
    while True:
        code, hours, rate = get_user_data()
        gross_pay, total_deductions, net_pay = perform_calculation(hours, rate)
        display_result(code, hours, gross_pay, total_deductions, net_pay)

        # ask user if they want to input data for another employee
        choice = input("Do you want to input data for another employee? (Y/N): ").upper()
        if choice != "Y":
            break
    
def get_user_data():
    code = input("Enter job category code (C, S, J, or M): ").upper()
    hours = float(input("Enter number of hours worked: "))
    if code not in pay_rates:
        print("Invalid job category code.")
        exit()
    rate = pay_rates[code][1]
    return code, hours, rate

def perform_calculation(hours, rate):
    gross_pay = hours * rate
    total_deductions = 0
    for deduction_name, deduction_rate in deductions.items():
        deduction_amount = gross_pay * deduction_rate
        total_deductions += deduction_amount
        print(f"{deduction_name} : ${deduction_amount:>8.2f}")
    net_pay = gross_pay - total_deductions
    return gross_pay, total_deductions, net_pay

def display_result(code, hours, gross_pay, total_deductions, net_pay):
    print("=" * 40)
    print("COMPANY NAME")
    print("=" * 40)
    print(f"Job category: {pay_rates[code][0]}")
    print(f"Hours worked : {hours:.2f}")
    print(f"Gross pay : ${gross_pay:>8.2f}")
    print(f"Total deductions : ${total_deductions:>8.2f}")
    print(f"Net pay : ${net_pay:>8.2f}")
    print("=" * 40)
    print(str(datetime.datetime.now()))

main()
 
