# Напишите функцию, которая определяет, сдал ли студент экзамен,
# и возвращает True, если сдал, и False – если не сдал.
#    Для успешной сдачи экзамена студенту необходимо иметь два зачёта,
#    а также получить балл не ниже 80 на самом экзамене.
#    Функция имеет три параметра – сдан ли первый зачёт,
#    сдан ли второй зачёт, полученный балл на экзамене. Вызовите
#    функцию несколько раз, передав ей различные аргументы,
#    и выведите результаты в консоль.

def is_passed_exam(is_first_test_passed, is_second_test_passed, exam_rate):
    return is_first_test_passed and is_second_test_passed and exam_rate >= 80

is_first_test_passed = True
is_second_test_passed = True
exam_rate = 80
print(is_passed_exam(is_first_test_passed, is_second_test_passed, exam_rate))

is_first_test_passed = False
is_second_test_passed = True
exam_rate = 80
print(is_passed_exam(is_first_test_passed, is_second_test_passed, exam_rate))

is_first_test_passed = True
is_second_test_passed = False
exam_rate = 80
print(is_passed_exam(is_first_test_passed, is_second_test_passed, exam_rate))

is_first_test_passed = True
is_second_test_passed = True
exam_rate = 65
print(is_passed_exam(is_first_test_passed, is_second_test_passed, exam_rate))

is_first_test_passed = False
is_second_test_passed = False
exam_rate = 65
print(is_passed_exam(is_first_test_passed, is_second_test_passed, exam_rate))