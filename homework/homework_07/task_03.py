# Напишите программу, которая помогает пользователю рассчитать общую стоимость поездки на автомобиле.
# Программа должна запрашивать у пользователя информацию о расстоянии до пункта назначения,
# расходе топлива на 100 км, цене топлива за литр и выводить итоговую стоимость поездки.
# Программа должна использовать функции и конкатенацию строк. Создайте функцию get_trip_info(), которая будет:

#   а. Запрашивать у пользователя расстояние до пункта назначения (в км), расход топлива на 100 км (в литрах) и цену топлива за литр.
#   б. Сохранять эти данные в отдельные переменные.
#   в. Вызывать функцию calculate_fuel_cost(distance, fuel_consumption, fuel_price), которая будет:
#       Возвращать общую стоимость топлива для поездки.
#       Затем функция get_trip_info() должна вызвать функцию generate_trip_report(distance, fuel_consumption, fuel_price, total_cost),
#           которая будет: Выводить отчёт о стоимости поездки, используя конкатенацию строк.

# Ожидаемый вывод при вызове функции get_trip_info():
#
#    Расстояние до пункта назначения: 300 км
#    Расход топлива: 8 л на 100 км
#    Цена топлива: 2 евро за литр
#    Общая стоимость топлива для поездки: 48 евро

def calculate_fuel_cost(distance, fuel_consumption, fuel_price):
    result = distance / 100 * fuel_consumption * fuel_price
    return round(result)


def generate_trip_report(distance, fuel_consumption, fuel_price, total_cost):
    print("Расстояние до пункта назначения: " + str(distance) + " км\n",
          "Расход топлива: " + str(fuel_consumption) + " л на 100 км\n",
          "Цена топлива: " + str(fuel_price) + " евро за литр\n",
          "Общая стоимость топлива для поездки: " + str(total_cost) + " евро",
          sep="")


def get_trip_info():
    distance = int(input("Укажите расстояние до пункта назначения (в км): "))
    fuel_consumption = int(input("Укажите расход топлива на 100 км (в литрах): "))
    fuel_price = int(input("Укажите цену топлива за литр: "))
    total_cost = calculate_fuel_cost(distance, fuel_consumption, fuel_price)
    generate_trip_report(distance, fuel_consumption, fuel_price, total_cost)


get_trip_info()
