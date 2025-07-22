numbers = [8, 4, 8, 3, 2, 5]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])

print("==========")

for i in numbers:
    print(i)

print("==========")

length = len(numbers)
i = 0

while i < length:
    print(numbers[i])
    i += 1