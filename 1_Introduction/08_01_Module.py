"""
A module is just a file with functions that we can referenced from other Python files
When we import a module the function names must have the module name plus . as a suffix: module.function
"""
import my_module  # Name of the module file

current_salary = 100000
new_salary = my_module.increase_salary(current_salary, 20)
print(current_salary, new_salary)

new_salary = my_module.add_bonus(current_salary, 44, 2, 1)
print(current_salary, new_salary)
