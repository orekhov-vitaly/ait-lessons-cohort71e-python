# Задача. Есть три разных имени, которые сохранены в переменные. Нужно поприветствовать каждого по миени по шаблону
# "Привет, <name>"

def print_greeting_person(name):
    print(f"Привет, {name}!")


name_1 = "Ваня"
name_2 = "Петр"
name_3 = "Иннокентий"

print_greeting_person(name_1)
print_greeting_person(name_2)
print_greeting_person(name_3)
print_greeting_person("Виталий")