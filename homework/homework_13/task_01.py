# Напишите программу, перемножающую чётные числа,
# которые вводит пользователь (пользователь может вводить любые числа).
# Программа должна перемножить любое количество чётных чисел, которое введёт пользователь.
# Ввод должен быть остановлен, если пользователь введёт ноль,
# после этого должен быть отображён на экране результат умножения.

result = 1

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break

    if number % 2 == 0:
        result *= number

print(result)