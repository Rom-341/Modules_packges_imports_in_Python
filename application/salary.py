from data import base_hours, overtime_rate, hourly_rate, hours_worked


"""# base_hours = 38  # Количество базовых часов
# overtime_rate = 1.5  # Коэффициент оплаты за сверхурочные часы
# hourly_rate = 100  # Ставка за каждый час работы
# hours_worked = 50  # Количество отработанных часов"""


def calculate_salary():
    """Вычисляем з/п при отработке базовых часов"""
    if hours_worked <= base_hours:
        salary = hours_worked * hourly_rate
    else:
        base_salary = base_hours * hourly_rate
        overtime_hours = hours_worked - base_hours
        overtime_salary = overtime_hours * hourly_rate * overtime_rate
        salary = base_salary + overtime_salary
        # print(salary)
    return salary


# calculate_salary()
