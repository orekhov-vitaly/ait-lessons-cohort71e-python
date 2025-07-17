# Напишите программу, которая выводит на экран числа от 15 до 1. Решения должно иметь два варианта (while/for)

print("=== While ===")
i = 15

while i > 0:
    print(i)
    i -= 1

print("\n=== For ===")
for i in range(15, 0, -1):
    print(i)

