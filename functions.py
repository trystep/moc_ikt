import time


# Отлов ошибок
def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e

    return inner


# Определение времени суток для приветсвенного сообщения
def times_of_day():
    '''
        Определение времени суток.
        Утро: с 5.00 до 12.00 включительно
        День: с 12.00 до 18.00 включительно
        Вечер: с 18.00 до 22.00 включительно
        Ночь: с 22.00 до 5.00 включительно
    '''
    time_list = time.localtime()
    hours = time_list[3]
    if 5 < int(hours) <= 12:
        return "Доброе утро!"
    elif 12 < int(hours) <= 18:
        return "Добрый день!"
    elif 18 < int(hours) <= 22:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"


###############################################################################################
# Вывод списка согласно ТЗ

electronics_list = ['Apple', 'Samsung', 'Nokia', 'Sony', 'Canon', 'Panasonic', 'Bose', 'Microsoft', 'LG', 'Intel',
                    'Nvidia', 'Dell', 'IBM', 'Acer', 'Asus', 'Lenovo', 'Xiaomi', 'Huawei']

electronics_list.sort()


def group(lst, n):
    """ Группировка элементов последовательности по n элементов """
    return ([lst[i:i + n] for i in range(0, len(lst), n)])


# Пагинация по 10 элементов списка на сообщение.
new_list = list(group(electronics_list, 10))

# Нумерация элементов списка
list_page_1 = [str(new_list[0].index(item) + 1) + ". " + item for item in new_list[0]]
list_page_2 = [str(new_list[1].index(item) + len(list_page_1) + 1) + ". " + item for item in new_list[1]]
###############################################################################################
