"""
Function that does not return a value
"""


def my_print(name: str, salary: float, age: int):
    print('[Name = {0}, Salary = {1}, Age = {2}]'.format(name, salary, age))


my_print("José Santos", 150000, 45)
my_print(age=45, name="José Santos", salary=150000)
my_print("Michael Jordan", 999999999, 50)
