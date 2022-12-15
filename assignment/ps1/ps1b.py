portion_down_payment = 0.25
r = 0.04
current_saving = 0

if __name__ == "__main__":
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary / 12

    num_of_month = 0

    while current_saving < down_payment:
        current_saving += current_saving * r / 12 + portion_saved * monthly_salary
        num_of_month += 1

        if num_of_month % 6 == 0:
            monthly_salary *= 1 + semi_annual_raise
    
    print(f"Number of months: {num_of_month}")
    
