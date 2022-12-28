from math import inf
semi_annual_raise = .07
r = 0.04
portion_down_ratio = 0.25
cost_of_house = 1000000

starting_salary = int(input("Enter the starting salary: "))

portion_down_payment =  portion_down_ratio * cost_of_house
monthly_salary = starting_salary/12

lower_bound = 0
upper_bound = 10000
step_count = 0

best_result = [inf,0]

while upper_bound - lower_bound >=0:
    step_count += 1

    current_savings = 0
    number_of_months = 0
    middle_point = int((lower_bound + upper_bound)/2)
    portion_saved = middle_point/10000

    while current_savings < portion_down_payment:
        current_savings += portion_saved * monthly_salary + current_savings * r/12
        number_of_months += 1

        if number_of_months % 6 == 0 :
            monthly_salary += semi_annual_raise * monthly_salary
    
    if number_of_months <= 36:
        upper_bound = middle_point-1

        if best_result[0] > middle_point:
            best_result[0] = middle_point
            best_result[1] = step_count

    else:
        lower_bound = middle_point + 1

if best_result[1] > 0:
    print(f"Best savings rate: 0.{best_result[0]}")
    print(f"Steps in bisection search: {best_result[1]}")
else:
    print("It is not possible to pay the down payment in three years")