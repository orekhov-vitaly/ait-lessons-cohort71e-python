# Петя и Вася сидели в баре. Петя заказал на сумму 100 у.е.,
# а Вася - на сумму 120 у.е.
#   Сохраните эти данные в переменные и напишите функцию,
#   которая считает общую сумму счёта
#   и выводит результат на экран

def print_total_sum(bill_1, bill_2):
    total_sum = bill_1 + bill_2
    print("Общая сумма счёта:", total_sum)


bill_person_1 = 100
bill_person_2 = 120

print_total_sum(bill_person_1, bill_person_2)