# Вам нужно перетащить тяжёлую мебель, помочь Вам может один из Ваших друзей - Петя или Вася.
# Напишите функцию, которая позволяет определить, сможете ли Вы перетащить мебель.
# Функция должна иметь два параметра – is_petya_free и is_vasya_free.
# Функция должна возвращать True, если мебель перетащить можно, и False – если нет.
# Мебель можно перетащить, если хотя бы один из друзей свободен. Создайте две переменные для каждого из друзей, содержащие значение, свободен ли Ваш друг.
# Вызовите функцию и выведите результат её работы на экран таким образом – «Получится ли перетащить мебель? – True/False».

def can_carry_furniture(is_petya_free, is_vasya_free):
    result = is_petya_free or is_vasya_free
    return result


is_petya_free = True
is_vasya_free = True
is_can_carry_furniture = can_carry_furniture(is_petya_free, is_vasya_free)
print("Получится ли перетащить мебель? -", is_can_carry_furniture)

is_petya_free = True
is_vasya_free = False
is_can_carry_furniture = can_carry_furniture(is_petya_free, is_vasya_free)
print("Получится ли перетащить мебель? -", is_can_carry_furniture)

is_petya_free = False
is_vasya_free = True
is_can_carry_furniture = can_carry_furniture(is_petya_free, is_vasya_free)
print("Получится ли перетащить мебель? -", is_can_carry_furniture)

is_petya_free = False
is_vasya_free = False
is_can_carry_furniture = can_carry_furniture(is_petya_free, is_vasya_free)
print("Получится ли перетащить мебель? -", is_can_carry_furniture)