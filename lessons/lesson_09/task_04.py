# Напишите функцию, которая проверяет на корректность адрес электронной почты,
#  и возвращает
#     True, если адрес корректен, и False – если нет.
#     Функция имеет один параметр – адрес электронной почты. Представим,
#     что адрес корректен, если:
#     он не менее 8 символов в длину,
#     содержит «@»,
#     содержит точку и не содержит «#».
#     Вызовите функцию несколько раз, передав ей различные аргументы,
#     и выведите результаты в консоль.

def is_email_correct(user_email):
    is_length_correct = len(user_email) > 7
    is_contain_at = "@" in user_email
    is_contain_dot = "." in user_email
    is_not_contain_hash = "#" in user_email
    result = is_length_correct and is_contain_at and is_contain_dot and not is_not_contain_hash
    return result

email = "qwe@gmail.com"
print(email, "-", is_email_correct(email))

email = "qe@gm.m"
print(email, "-", is_email_correct(email))

email = "qwegmail.com"
print(email, "-", is_email_correct(email))

email = "qweg@mailcom"
print(email, "-", is_email_correct(email))

email = "qwe@gmail.c#om"
print(email, "-", is_email_correct(email))