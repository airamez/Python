import my_module
"""
If a function will be used multiple time we can add assign a local name for it
"""
bonus = my_module.add_bonus

current_salary = 100000

new_salary = bonus(current_salary, 44, 2, 1)
print(current_salary, new_salary)
