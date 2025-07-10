# Напишите функцию, которая определяет, нужно ли сегодня идти на работу.
# Функция должна возвращать True, если нужно, и False – если нет.
# Функция должна иметь два параметра – is_working_day и is_vacation.
# На работу нужно идти, если рабочий день и Вы не в отпуске.
# Создайте две переменные, которые содержат информацию, рабочий ли день и в отпуске ли Вы сейчас.
# Вызовите функцию и выведите результат её работы на экран таким образом – «Нужно ли сегодня идти на работу? – True/False».

def need_working(is_working_day, is_vacation):
    resalt = is_working_day and not(is_vacation)
    return resalt

is_working_day = True
is_vacation = True
is_need_working = need_working(is_working_day, is_vacation)
print("Нужно ли сегодня идти на работу? -", is_need_working)

is_working_day = True
is_vacation = False
is_need_working = need_working(is_working_day, is_vacation)
print("Нужно ли сегодня идти на работу? -", is_need_working)

is_working_day = False
is_vacation = True
is_need_working = need_working(is_working_day, is_vacation)
print("Нужно ли сегодня идти на работу? -", is_need_working)

is_working_day = False
is_vacation = False
is_need_working = need_working(is_working_day, is_vacation)
print("Нужно ли сегодня идти на работу? -", is_need_working)