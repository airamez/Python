"""
Read the Name, employment length (Years) and the current salary of an employee and calculate the
new salary based on the information below:
    Employment length	Salary increment
    0 to 2 years			1%
    3 to 4 years			2%
    5 to 10 years			3%
    above 10 years			5%

    Salary range	Salary increment
    0 to 45,000		    5%
    45,001 to 80,000	3%
    80,001 to 100,000	2%
    100,000 and above	1%
"""

name = input("Name = ")
employment_length = int(input("Employment length = "))
current_salary = float(input("Salary = "))

employment_length_increment = None
if employment_length <= 2:
    employment_length_increment = 1
elif employment_length <= 4:
    employment_length_increment = 2
elif employment_length <= 10:
    employment_length_increment = 3
else:
    employment_length_increment = 5

salary_range_increment = None
if current_salary <= 45000:
    salary_range_increment = 5
elif current_salary <= 80000:
    salary_range_increment = 3
elif current_salary <= 100000:
    salary_range_increment = 2
else:
    salary_range_increment = 1

salary_increment_percentage = (employment_length_increment + salary_range_increment) / 100
salary_increment = current_salary * salary_increment_percentage
new_salary = current_salary + salary_increment

print("New Salary = {0}; Salary Increment = {1}".format(new_salary, salary_increment))
