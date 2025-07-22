# Есть список чисел - [5, 8, -4, 3, 9, -5, 1]
# Задача: найти и вывести на экран все отрицательные числа в списке

numbers = [5, 8, -4, 3, 9, -5, 1]

for number in numbers:
    if number < 0:
        print(number)

print("========")

for number in numbers:
    if number >= 0:
        continue
    print(number)