# Напишите функцию, которая определяет, открыт ли офис.
# Функция должна возвращать True, если открыт, и False – если нет.
# Функция должна иметь три параметра – hours, is_weekend, is_holiday.
# Офис открыт в любой день, кроме выходных и праздников, если на часах время в диапазоне либо с 8 до 12 ч. включительно,
# либо с 14 до 18 ч. включительно (учитываем только часы, без минут).
# Вызовите функцию и выведите результат её работы на экран таким образом – «Офис открыт? – True/False».

def is_office_open(hours, is_weekend, is_holiday):
    is_open_hours = (8 <= hours <= 12) or (14 <= hours <= 18)
    result = is_open_hours and not is_weekend and not is_holiday
    return result


time = 8
is_weekend = True
is_holiday = True
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 8
is_weekend = False
is_holiday = True
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 8
is_weekend = True
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 8
is_weekend = False
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 6
is_weekend = False
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 12
is_weekend = False
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 13
is_weekend = False
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 18
is_weekend = False
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)

time = 19
is_weekend = False
is_holiday = False
office_open = is_office_open(time, is_weekend, is_holiday)
print("Офис открыт? –", office_open)