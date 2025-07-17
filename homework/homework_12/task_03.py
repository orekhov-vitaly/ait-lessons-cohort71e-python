# Напишите программу, которая запрашивает у пользователя целое число N,
# вычисляет первые N чисел последовательности Фибоначчи и выводит их на экран.
# Числа Фибоначчи — это последовательность,
# где каждое число является суммой двух предыдущих, начиная с чисел 0 и 1.

count = int(input("Какое количество чисел Фибоначчи вывести? "))

num_prev = 0
print(num_prev)
num_current = 1
print(num_current)

for i in range(2, count):
    num_next = num_prev + num_current
    num_prev = num_current
    num_current = num_next
    print(num_next)