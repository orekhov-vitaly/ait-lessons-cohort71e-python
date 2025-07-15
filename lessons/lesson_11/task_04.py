# Напишите функцию с тремя параметрами - первое число, второе число и действие.
#    Действие может быть +, -, * или /.
#    В зависимости от переданного третьего параметра программа
#    должна выполнить соответствующее действие с двумя числами и
#    вернуть результат. Запросите эти данные у пользователя,
#    вызовите функцию и выведите результат на экран.


def calculate(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "/":
        if num_2 == 0:
            return "На ноль делить нельзя!"
        return num_1 / num_2
    else:
        return "Вы ввели неподдерживаемую операцию!"


numer_1 = int(input("Первое число: "))
numer_2 = int(input("Второе число: "))
action = input("Укажите действие: ")
result = calculate(numer_1, numer_2, action)

print(result)