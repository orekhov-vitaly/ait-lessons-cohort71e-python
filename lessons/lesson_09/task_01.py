# Напишите функцию, которой можно передать целое число.
# Функция должна возвращать True, если число положительное чётное
#    либо отрицательное. В остальных случаях функция должна возвращать False.
#    Вызовите функцию несколько раз, передав ей
#    различные аргументы, и выведите результаты в консоль.

def check_number(num):
    result = num < 0 or (num > 0 and num % 2 == 0)
    return result


a = 3
print(a, "-", check_number(a))

a = 1
print(a, "-", check_number(a))

a = 0
print(a, "-", check_number(a))

a = 2
print(a, "-", check_number(a))

a = -1
print(a, "-", check_number(a))

a = -2
print(a, "-", check_number(a))
