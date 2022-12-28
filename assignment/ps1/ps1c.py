# I didn't use function because it's not covered in the course yet.

from math import inf

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000

if __name__ == "__main__":
    annual_salary = int(input("Enter your annual salary: "))

    search_upper_bound = 10000
    search_lower_bound = 0

    is_solution_found = False
    step_count = 0
    down_payment = total_cost * portion_down_payment

    best_result = [inf, 0]  # [portion_saved * 10000, step_count]

    while (search_upper_bound - search_lower_bound) >= 0:
        step_count += 1

        # calculate saving in 36 month
        current_saving = 0
        num_of_month = 0
        search_pivot = int((search_upper_bound + search_lower_bound) / 2)
        portion_saved = search_pivot / 10000
        monthly_salary = annual_salary / 12

        while current_saving < down_payment:
            current_saving += current_saving * r /12 + portion_saved * monthly_salary
            num_of_month += 1

            if num_of_month % 6 == 0:
                monthly_salary *= 1 + semi_annual_raise
        
        if num_of_month <= 36:
            is_solution_found = True
            search_upper_bound = search_pivot - 1

            if best_result[0] > search_pivot:
                best_result[0] = search_pivot
                best_result[1] = step_count

        else:
            search_lower_bound = search_pivot + 1
    
    if is_solution_found:
        print(f"Best savings rate: 0.{best_result[0]}")
        print(f"Steps in bisection search: {best_result[1]}")
    else:
        print("It is not possible to pay the down payment in three years.")

    