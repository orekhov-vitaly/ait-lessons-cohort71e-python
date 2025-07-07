# Исходные данные: есть длина и ширина погрузочного пространства корабля, а также длина и ширина морского контейнера. Напишите программу, которая запрашивает эти данные у пользователя, сохраняет эти данные в переменных, вычисляет и выводит в консоль, сколько контейнеров может перевезти корабль.

loading_space_length = float(input("Укажите длину погрузочного пространства корабля: "))
loading_space_width = float(input("Укажите ширину погрузочного пространства корабля: "))
container_length = float(input("Укажите длину морского контейнера: "))
container_width = float(input("Укажите ширину морского контейнера: "))

count_containers_in_length = loading_space_length // container_length
count_containers_in_width = loading_space_width // container_width

count_containers = int(count_containers_in_length * count_containers_in_width)

print("Количество контейнеров, которое может перевезти корабль:", count_containers)