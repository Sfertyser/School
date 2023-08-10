# Task 1
import random
# Блок для створення списку.
random_number = random.randint(1, 1000)  # Створює рандомне число для random.seed
random.seed(random_number)  # Генерує список заповненим випадковими числами.
n = 30  # Кількість чисел у списку.
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
index3_product = 1  # Змінна для добутка елементів з кратними індексами 3.
for i in range(2, len(numbers), 3):  # Вибирає елементи зі списку індекс який кратний 3.
    index3_product *= numbers[i]  # Перемножує число зі змінною.
print("Добуток елементів з кратними індексами 3:", index3_product)  # Виводить добуток елементів з кратними індексами 3.

# Блок для обчислення добутка елементів між мінімальним та максимальним елементом.
min_num = min(numbers)  # Вибирає мінимальне число зі списку.
max_num = max(numbers)  # Вибирає максимальне число зі списку.
min_max_number = 1  # Змінна для добутка елементів.
for x in numbers[numbers.index(min_num) + 1: numbers.index(max_num)]:
    min_max_number *= x
print("Добуток елементів між мінімальним та максимальним елементом:", min_max_number)

# Обчислюємо суму елементів між першим та останнім позитивними елементами
first_positive_index = None
last_positive_index = None
for i, x in enumerate(numbers):
    if x > 0:
        first_positive_index = i
        break
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break
sum_between_positives = 0
if first_positive_index is not None and last_positive_index is not None:
    for x in numbers[first_positive_index + 1: last_positive_index]:
        sum_between_positives += x
print("Сума елементів між першим та останнім позитивними елементами:", sum_between_positives)
