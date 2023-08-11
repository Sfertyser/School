# Task 1
import random
try:
    # Блок для створення списку.
    random_number = random.randint(1, 1000)  # Створює рандомне число для random.seed
    random.seed(random_number)  # Генерує список заповненим випадковими числами.
    n = 10  # Кількість чисел у списку.
    numbers = [random.randint(-1000, 1000) for _ in range(n)]  # Вибирає рандомне число для всіх елементів.
    print(f"Список чисел: {numbers}")  # Виводить створенні числа.
    # Блок для обчислення суми негативних чисел.
    negative_sum = 0  # Створюємо змінну для суми негативних чисел.
    for x in numbers:  # Звертається до кожного елементу в листі.
        if x < 0:  # Якщо елемент списку менший за нуль.
            negative_sum += x  # Добавляє число до змінної.
    print(f"Сума негативних чисел: {negative_sum}")  # Виводимо суму негативних чисел.

    # Блок для обчислення суми парних та непарних чисел.
    even_sum = 0  # Створюємо змінну для суми парних чисел.
    odd_sum = 0  # Створюємо змінну для суми непарних чисел.
    for x in numbers:  # Звертається до кожного елементу в листі.
        if x % 2 == 0:  # Якщо число зі списку ділиться на 2 без залишку.
            even_sum += x  # Добавляємо число до суми парних чисел.
        else:  # Інакше
            odd_sum += x  # Добавляємо число до суми непарних чисел.
    print(f"Сума парних чисел: {even_sum}")  # Виводимо суму парних чисел.
    print(f"Сума непарних чисел: {odd_sum}")  # Виводимо суму непарних чисел.

    # Блок для обчислення добутка елементів з кратними індексами 3.
    index3_number = 1  # Змінна для добутка елементів з кратними індексами 3.
    for i in range(2, len(numbers), 3):  # Вибирає елементи зі списку індекс який кратний 3.
        index3_number *= numbers[i]  # Перемножує число зі змінною.
    print(f"Добуток елементів з кратними індексами 3: {index3_number}")  # Виводить добуток елементів.

    # Блок для обчислення добутка елементів між мінімальним та максимальним елементом.
    min_num = min(numbers)  # Вибирає мінимальне число зі списку.
    max_num = max(numbers)  # Вибирає максимальне число зі списку.
    min_max_number = 1  # Змінна для добутка елементів.
    for x in numbers[numbers.index(min_num) + 1: numbers.index(max_num)]:  # Шукає чи є елементи між ними.
        min_max_number *= x  # Якщо є то перемножує зі змінною.
    if min_max_number == 1:  # Якщо між елементами немає інших елементів.
        print(f"Між мінімальним та максимальним елементом немає інших елементів.")  # Виводить це.
    else:  # Інакше
        print(f"Добуток елементів між мінімальним та максимальним елементом:: {min_max_number}")  # Виводить це.

    # Блок для обчислення суми елементів між першим та останнім позитивними елементами
    first_positive_number = 0  # Змінна для першого позитивного числа.
    last_positive_number = 0  # Змінна для останнього позитивного числа.
    for i, x in numbers:  # Звертається до елементів зі списку.
        if x > 0:  # Якщо число більше за нуль.
            first_positive_number = i  # Заноситься до змінної.
            break  # Виходить з циклу.
    for i in range(len(numbers) - 1, -1, -1):  # Цей цикл шукає елемент починаючи з останнього елементу.
        if numbers[i] > 0:  # Якщо число більше за нуль.
            last_positive_number = i  # Заноситься до змінної.
            break  # Виходить з циклу.
    sum_between_numbers = 0  # Змінна для суми елементів.
    if first_positive_number == 0 or last_positive_number == 0:  # Якщо змінні не дорівнюють нулю.
        print(f"В Списку недостатньо позитивних елементів.")
    else:
        for x in numbers[first_positive_number + 1: last_positive_number]:  # Шукає числа між ними.
            sum_between_numbers += x  # Добавляє їх в змінну.
        print(f"Сума елементів між першим та останнім позитивними елементами: {sum_between_numbers}")  # Виводить суму.
except Exception as error:
    print("Помилка! зв'яжіться з розробником програми.")


# Task 2
# Генеруємо список випадкових цілих чисел
# random_numbers = [random.randint(-100, 100) for _ in range(20)]
#
# # Створюємо списки для зберігання різних типів чисел
# even_numbers = []
# odd_numbers = []
# negative_numbers = []
# positive_numbers = []
#
# # Розділяємо числа відповідно до їхнього типу
# for num in random_numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
#     if num < 0:
#         negative_numbers.append(num)
#     elif num > 0:
#         positive_numbers.append(num)
#
# # Виводимо результати
# print("Список випадкових чисел:", random_numbers)
# print("Список парних чисел:", even_numbers)
# print("Список непарних чисел:", odd_numbers)
# print("Список негативних чисел:", negative_numbers)
# print("Список позитивних чисел:", positive_numbers)
#
# # Task Matrix
# # Створюємо матрицю 10x10 та заповнюємо рандомними значеннями від 10 до 99
# matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]
#
# # Виводимо матрицю
# print("Матриця 10x10:")
# for row in matrix:
#     print(row)
#
# # Знаходимо та виводимо суму чисел головної діагоналі
# main_diagonal_sum = sum(matrix[i][i] for i in range(10))
# print("Сума чисел головної діагоналі:", main_diagonal_sum)
#
# # Знаходимо та виводимо мінімальне та максимальне значення побічної діагоналі
# secondary_diagonal_values = [matrix[i][9 - i] for i in range(10)]
# min_secondary = min(secondary_diagonal_values)
# max_secondary = max(secondary_diagonal_values)
# print("Мінімальне значення побічної діагоналі:", min_secondary)
# print("Максимальне значення побічної діагоналі:", max_secondary)
#
# # Ввід номера стовпця та вивід цифр з цього стовпця
# column_number = int(input("Введіть номер стовпця (0-9): "))
# column_values = [matrix[i][column_number] for i in range(10)]
# print(f"Значення зі стовпця {column_number}: {column_values}")
#
# # Ввід номера двох стовпців та обмін їх місцями
# swap_column1 = int(input("Введіть номер першого стовпця (0-9): "))
# swap_column2 = int(input("Введіть номер другого стовпця (0-9): "))
# for i in range(10):
#     matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]
#
# # Виводимо змінену матрицю
# print("Матриця після обміну стовпців:")
# for row in matrix:
#     print(row)
