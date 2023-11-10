"""1. Наведено список чисел. Визначте, скільки у ньому зустрічається різних чисел.
приклад: якщо в списку число 8 зустрічається 3 рази то це означає що в списку зустрічається 8мка."""

# import random
#
# numbers = [random.randint(0, 20) for _ in range(10)]
# different_numbers = set(numbers)
# similar_numbers = len(different_numbers)
# print(similar_numbers)

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3, 4, 10, 11, 12, 13, 14, 15}
# # Додавання елементу
# set1.add(6)
# print(set1)
# # Видалення елементу
# set1.remove(3)
# print(set1)
# set1.remove(6)
# print(set1)
# # Об'єднання множин
# union_set = set1.union(set2)
# print(union_set)
# # Перевірка елемента у множині
# member = 4 in set1
# print(member)
# # Перетин множин
# intersection_set = set1.intersection(set2)
# print(intersection_set)
# # Різниця множин
# difference_set = set1.difference(set2)
# print(difference_set)

"""2. Дано два списки чисел. Порахуйте, скільки різних чисел міститься як у першому списку, і у другому оночасно.
-PS: Різних чисел - мається на увазі що усі однакові елементи повинні бути представленні в одному екземплярі
(приклад: 3 однаковиі числа мають бути пораховані як 1 елемент)"""
# text1 = [1, 2, 3, 4, 5, 6, 7, 8]
# text2 = [5, 6, 7, 8, 9, 10, 11, 12]
# different_num1 = set(text1)
# different_num2 = set(text2)
# difference_set = different_num1.intersection(different_num2)
# difference = len(difference_set)
# print(difference)

""" 3. Є список(створити тестовий список для перевірки) із довільними даними (можуть бути словніки і списки).
Поставлено завдання перетворити його на множину. Якщо якісь елементи не можна хешувати, пропускаємо їх."""
text1 = ["abc", 5, 89, {"author": "book"}]
text2 = set()
for i in text1:
    if isinstance(i, (str, int)):
        text2.add(i)
print(text2)
