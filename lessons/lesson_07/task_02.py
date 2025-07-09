# Напишите программу, которая запрашивает у пользователя следующие данные:
#     - заработная плата сотрудника в час,
#     - количество часов, которые отработал сотрудник,
#     - размер фиксированной премии сотруднику,
#     - ставка подоходного налога.
#    Напишите программу, которая сохраняет эти данные в переменных,
#    вычисляет и выводит в консоль, какую заработную
#    плату получит сотрудник.
#    При этом программа должна содержать две функции -
#    для расчёта заработной платы брутто и нетто.

def get_salary_brutto(salary_per_hour, hours, bonus):
    return salary_per_hour * hours + bonus


def get_salary_netton(salary, tax_rate):
    return salary - salary * tax_rate / 100


salary_per_hour = float(input("Заработная плата сотрудника в час: "))
hours = int(input("Количество часов, которые отработал сотрудник: "))
bonus = float(input("Размер фиксированной премии сотруднику: "))
tax_rate = float(input("Ставка подоходного налога, %: "))

salary_brutto = get_salary_brutto(salary_per_hour, hours, bonus)
salary_netto = get_salary_netton(salary_brutto, tax_rate)

print("Заработная плата до вычета налогов:", salary_brutto, "у.е.")
print("Заработная плата после вычета налогов:", salary_netto, "у.е.")
