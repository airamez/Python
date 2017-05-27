"""
It is possible to import specific functions directly from a module
"""
from my_module import add_bonus

current_salary = 100000

new_salary = add_bonus(current_salary, 44, 2, 1)
print(current_salary, new_salary)
