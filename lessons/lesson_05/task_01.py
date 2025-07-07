# 2.3 Исходные данные: курс евро к доллару - 1.09.
#    Килограмм печенья стоит 3 доллара 25 центов.
#    Килограмм вафель стоит 4 доллара 40 центов. Вам нужно купить
#    полкилограмма печенья и полтора килограмма вафель.
#    У Вас есть 10 евро. Напишите программу, которая считает, сколько
#    денег у Вас останется в евро.

warehous_width = float(input("Введите ширину склада: "))
warehous_length = float(input("Введите длину склада: "))
table_width = float(input("Введите ширину стола: "))
table_length = float(input("Введите длину стола: "))

tables_in_length = warehous_length // table_length
tables_in_width = warehous_width // table_width

tables_count = tables_in_length * tables_in_width

print(tables_count)