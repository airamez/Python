def increase_salary(current_salary, increase_percent):
    return current_salary + current_salary * increase_percent / 100


def add_bonus(current_salary, age, years_of_work, dependents):
    bonus = 0
    if age > 40:
        bonus += 5
    else:
        bonus += 10
    if years_of_work >= 5:
        bonus += 5
    else:
        bonus += 10
    bonus += dependents / 100
    return increase_salary(current_salary, bonus)
