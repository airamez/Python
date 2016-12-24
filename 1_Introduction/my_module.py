def increase_salary(current_salary, increase_percent):
    """
    Increase a salary based on a percentage value
    :param current_salary: current salary
    :param increase_percent: increase percentage value
    :return: increased salary
    """
    return current_salary + current_salary * increase_percent / 100


def add_bonus(current_salary, age, years_of_work, dependents):
    """
    Add bonus do a salary
    :param current_salary: current salary
    :param age: age
    :param years_of_work: years working for the company
    :param dependents: number of dependents
    :return: new salary with bonus added
    """
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
