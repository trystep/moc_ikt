import time
import datetime


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
def times_of_day(dt=None, ts=None, tod_dict=None):
    '''
    Принимает объект datetime (dt) или timestamp (ts), и словарь tod_dict {час : наименование времени}
    Возвращает строку c приветственным сообщением и временем суток.

    При отсутствии аргументов - возвращает строку с приветственным сообщением,
    где первый элемент "Добрый", а второй элемент соответствует времени суток, то есть утро, день, вечер и ночь
    в зависимости от времени

        «утро» — с 0.00 до 12.00,
        «день» — с 12.00 до 18.00,
        «вечер» — с 18.00  до 21.00,
        «ночь» - с 21.00  до 0.00,

    Eсли час не отражен в словаре, возвращает None
    Требует import datetime.


    '''
    morning = "Доброе утро!"
    day = "Добрый день!"
    evening = "Добрый вечер!"
    night = "Доброй ночи!"

    # определение словаря
    if tod_dict:
        pass
    else:
        tod_dict = {0: morning,
                    1: morning,
                    2: morning,
                    3: morning,
                    4: morning,
                    5: morning,
                    6: morning,
                    7: morning,
                    8: morning,
                    9: morning,
                    10: morning,
                    11: morning,
                    12: day,
                    13: day,
                    14: day,
                    15: day,
                    16: day,
                    17: day,
                    18: evening,
                    19: evening,
                    20: evening,
                    21: night,
                    22: night,
                    23: night}

    # определение оцениваемого времени
    if dt:
        if isinstance(dt, datetime.datetime):
            dt = dt
        else:
            print('некорректный формат dt: %s \n требуется объект datetime.datetime' % (type(dt)))
            return None
    elif ts:
        if isinstance(ts, (int, float)):
            if ts > 0:
                dt = datetime.datetime.fromtimestamp(ts)
                print(dt.ctime())
            else:
                print('отрицательное значение ts недопустимо')
                return None
        else:
            print('некорректный формат ts: %s \n требуется значение int или float' % (type(ts)))
            return None
    else:
        dt = datetime.datetime.now()
    h = dt.hour

    # подбор
    if h in tod_dict:
        tod = tod_dict[h]
        return tod
    else:
        print('Значение времени отсутствует в словаре')
        return None



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
