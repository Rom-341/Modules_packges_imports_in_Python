from application.db.people import get_employees
from application.salary import calculate_salary


def main():
    print("Общая сумма заработка:", calculate_salary())
    print(f'Заработная плата до налогового вычета  {get_employees()} составляет {calculate_salary()}')



if __name__ == '__main__':
    main()
