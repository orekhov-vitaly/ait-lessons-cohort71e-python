# Напишите функцию, которой можно передать целое число.
# Функция должна возвращать True, если число попадает в диапазон от 10 до 30 включительно.
# В остальных случаях функция должна возвращать False.
# Вызовите функцию несколько раз, передав ей различные аргументы, и выведите результаты в консоль.

def is_num_exist_range(num):
    return 10 <= num <= 30


print(is_num_exist_range(0))
print(is_num_exist_range(9))
print(is_num_exist_range(10))
print(is_num_exist_range(15))
print(is_num_exist_range(30))
print(is_num_exist_range(31))