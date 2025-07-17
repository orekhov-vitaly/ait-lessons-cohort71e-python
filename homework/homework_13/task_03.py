# Доработайте вторую задачу таким образом,
# чтобы у пользователя было только пять попыток ввода.
# После пятой некорректной попытки программа
# должна завершаться с сообщением "Ошибка регистрации!".

new_password = None

for i in range(5, 0, -1):
    temporary_password = input("Придумайте пароль не менее 8 символов (осталось попыток: " + str(i) + "): ")
    if len(temporary_password) >= 8:
        new_password = temporary_password
        break
    if i <= 1:
        break
    print("Попробуйте ещё раз")

if None != new_password:
    print("Пароль сохранен!")
else:
    print("Ошибка регистрации!")