# Напишите функцию, которая определяет, можно ли сейчас идти гулять.
#     Функция должна возвращать
#     True, если гулять можно, и False – если нельзя.
#     Функция должна иметь два параметра – is_weekend и is_rain. Гулять
#     можно идти, если сейчас выходные и нет дождя.
#     Создайте две переменные, которые содержат информацию, выходной ли
#     сейчас и идёт ли сейчас дождь.
#     Вызовите функцию и выведите результат её работы на экран таким образом – «Можно ли сейчас гулять? – True/False».

def is_can_walking(is_weekend, is_rain):
    return is_weekend and not is_rain

weekend = True
raining = True
print("Можно ли сейчас гулять? –", is_can_walking(weekend, raining))

weekend = True
raining = False
print("Можно ли сейчас гулять? –", is_can_walking(weekend, raining))

weekend = False
raining = True
print("Можно ли сейчас гулять? –", is_can_walking(weekend, raining))

weekend = False
raining = False
print("Можно ли сейчас гулять? –", is_can_walking(weekend, raining))