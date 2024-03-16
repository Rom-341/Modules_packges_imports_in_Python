first_name =input('Введите фамилию сотрудника: ')
name =input('Введите имя сотрудника: ')


def get_employees():
    my_dict = {
        first_name: name,
        }
    for key, value in my_dict.items():
        # print(key, value)

        return key, value


# get_employees()
git