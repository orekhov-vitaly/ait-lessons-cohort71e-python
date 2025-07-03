# Исходные данные: конфета стоит 3 у.е., у Вас есть 27 у.е. Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько конфет Вы можете купить.
print("===Task 1===")

price = 3
balance = 27
count = balance // price
print("Вы можете купить конфет: ", count, " (шт.)")

print("============\n")

# Исходные данные: конфета стоит 3 у.е., мороженое стоит 5 у.е. Вы хотите купить 7 конфет и 3 мороженых. Напишите программу, которая сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько денег Вам потребуется.
print("===Task 2===")

candy_price = 3
ice_price = 5
candy_count = 7
ice_count = 3
candy_sum = candy_price * candy_count
ice_sum = ice_price * ice_count
print("Мороженное:", ice_count,"шт. по", ice_price, "у.е - необходимо", ice_sum, "у.е")
print("Конфеты:", candy_count,"шт. по", candy_price, "у.е - необходимо", candy_sum, "у.е")

print("============\n")

# *** (задание повышенной сложности, необязательное, только для желающих). Исходные данные: курс евро к доллару - 1.09. Килограмм печенья стоит 3 доллара 25 центов. Килограмм вафель стоит 4 доллара 40 центов. Вам нужно купить полкилограмма печенья и полтора килограмма вафель. У Вас есть 10 евро. Напишите программу, которая считает, сколько денег у Вас останется в евро.
print("===Task 3===")

rate_euro_usd = 1.09
balance_euro = 10

coockie_price_usd = 3.25
coockie_price_euro = coockie_price_usd / rate_euro_usd
coockie_need = 0.5

vafli_price_usd = 4.4
vafli_price_euro = vafli_price_usd / rate_euro_usd
vafli_need = 1.5

coockie_sum = coockie_price_euro * coockie_need
vafli_sum = vafli_price_euro * vafli_need
balance_euro = balance_euro - coockie_sum - vafli_sum
print("€", balance_euro)

print("============\n")
