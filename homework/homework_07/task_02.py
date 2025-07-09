# Бананы стоят 11 у.е., яблоки - 8 у.е.
# Вам нужно купить два килограмма бананов и три килограмма яблок.
# Сохраните все эти данные в переменных. Напишите программу,
# которая выводит на экран фразу
# "Для покупки Х килограммов бананов и Х килограммов яблок мне нужно Х у.е."
# В местах, где Х - нужно воспользоваться переменными.
# Напишите отдельную функцию, которая считает стоимость продукта
# и воспользуйтесь ей два раза для расчёта стоимости яблок и бананов.

def get_total_price(price, count):
    return price * count


banana_price = 11
apple_price = 8

banana_count = 2
apple_count = 3

banana_total_cost = get_total_price(banana_price, banana_count)
apple_total_cost = get_total_price(apple_price, apple_count)

common_price = banana_total_cost + apple_total_cost

print("Для покупки", banana_count, "килограммов бананов и", apple_count, "килограммов яблок мне нужно", common_price, "у.е.")