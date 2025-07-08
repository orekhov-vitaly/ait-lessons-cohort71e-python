# Исходные данные: конфета стоит 3 у.е., мороженое стоит 5 у.е.
# Вы хотите купить 7 конфет и 3 мороженых.
# Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько денег Вам потребуется.
# При этом программа должна содержать отдельную функцию, которая считает итоговую стоимость продукта, принимая на вход его количество и цену.
# Данной функцией нужно воспользоваться два раза для конфет и мороженого.

def get_product_sum(price, count):
    return price * count

def get_total_sum(val_1, val_2):
    return val_1 + val_2

candy_price = 3
ice_cream_price = 5
candy_count = 7
ice_cream_count = 3

candy_total_sum = get_product_sum(candy_price, candy_count)
ice_cream_total_sum = get_product_sum(ice_cream_price, ice_cream_count)
total_sum = get_total_sum(candy_total_sum, ice_cream_total_sum)

print("Для конфет потребуется", candy_total_sum, "у.е.")
print("Для мороженого потребуется", ice_cream_total_sum, "у.е.")
print("Всего необходимо", total_sum, "у.е.")