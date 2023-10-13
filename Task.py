# Задача 1
# text = input("Введіть рядок з 15 символами: ")
# if not text:
#     print("Помилка! рядок порожній.")
# else:
#     if len(text) < 15:
#         text *= (15//len(text))+1
# text_list = list(text)
# print(text_list)
# print(text_list[-5:])
# print(text_list[::-1])
# print(text_list[::2])
# print(text_list[:5]+text_list[-5:])

# Задача 2
# user_input = input("Введiть строку з 15 символiв: ")
# if not user_input:
#     print("Строка порожня!")
# else:
#     user_input = user_input.just(15, user_input * 15)[:15]
# user_list = list(user_input)
# print(user_list)

# Задача 2 перероблена
user_input = input("Введiть строку з 15 символiв: ")
if not user_input:
    print("Строка порожня!")
else:
    user_input = user_input.ljust(15)[:15]
user_list = list(user_input)
print(user_list)
