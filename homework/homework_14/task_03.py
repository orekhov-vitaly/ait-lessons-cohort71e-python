# Напишите функцию, которая принимает на вход список чисел, находит в нём максимальное и минимальное значения, и меняет их местами.

def change_list(list):
    index = 0
    max_value_index = 0
    min_value_index = 0

    while index < len(list):
        if list[index] > list[max_value_index]:
            max_value_index = index
        if list[index] < list[min_value_index]:
            min_value_index = index
        index += 1

    min_value = list[min_value_index]
    list[min_value_index] = list[max_value_index]
    list[max_value_index] = min_value
    return list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 123, 432, 236, 6]
print(numbers)

print(change_list(numbers))