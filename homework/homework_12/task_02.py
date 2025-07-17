# Напишите программу, которая выводит на экран все чётные числа в порядке убывания из диапазона от 100 до 80.

print("=== for var 1 ===")

for i in range(100, 79, -2):
    print(i)


print("\n=== for var 2 ===")

for i in range(100, 79, -1):
    if i % 2 == 0:
        print(i)

print("\n=== while var 1 ===")

i = 100
while i > 79:
    print(i)
    i += -2

print("\n=== while var 2 ===")

i = 100
while i > 79:
    if i % 2 == 0:
        print(i)
    i += -1
