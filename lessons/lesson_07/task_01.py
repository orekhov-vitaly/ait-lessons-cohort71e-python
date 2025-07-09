# Исходные данные: есть склад размером 30 на 40 и высотой 20,
# размер коробки – 5 х 8 х 4. Напишите программу, которая
#    сохраняет эти данные в переменных, вычисляет и выводит в консоль,
#    сколько коробок поместится на склад. В программе
#    должна быть отдельная функция, которая вычисляет объём
#    (независимо от того, объём чего вычисляется, коробки или
#    склада).

def get_volume(w, l, h):
    vol = w * l * h
    return vol


storage_width = 30
storage_length = 40
storage_height = 20
box_width = 5
box_length = 8
box_height = 4

storage_volume = get_volume(storage_width, storage_length, storage_height)
box_volume = get_volume(box_width, box_length, box_height)

boxes_count = storage_volume // box_volume

print("Storage volume:", storage_volume)
print("Box volume:", box_volume)
print(boxes_count)
