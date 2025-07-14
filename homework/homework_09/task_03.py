# Напишите функцию, которая принимает четыре числа в качестве параметров.
# Функция должна возвращать True в том случае, если первое число делится без остатка на второе, а третье при этом на четвёртое.
# Также функция должна возвращать True, если второе и четвёртое числа являются нечётными.
# Во всех остальных случаях функция должна возвращать False.
# Передайте в функцию три разных набора чисел и выведите результаты на экран.

def check_numbers(num_1, num_2, num_3, num_4):
    condition_1 = num_1 % num_2 == 0 and num_3 % num_4 == 0
    condition_2 = num_2 % 2 != 0 and num_4 % 2 != 0
    return condition_1 or condition_2


print(check_numbers(4, 2, 6, 3))
print(check_numbers(8, 3, 7, 5))
print(check_numbers(4, 2, 7, 4))
print(check_numbers(5, 2, 8, 4))
print(check_numbers(9, 6, 8, 4))
print(check_numbers(9, 6, 8, 4))