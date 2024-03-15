# 1
dictionary = {
    1: {"Ім`я": "Максим", "Прізвище": "Дарієнко", "Вік": "15"},
    2: {"Ім`я": "Каріна", "Прізвище": "Хорошун", "Вік": "16"},
    3: {"Ім`я": "Дмитро", "Прізвище": "Агоштон", "Вік": "15"},
    4: 10,  # {"Ім`я": "Олександр", "Прізвище": "Мандзюк", "Вік": "14"},
    5: {"Ім`я": "Назар", "Прізвище": "Калуга", "Вік": "14"}
             }

# 2
# name = "Дмитро"
# for person_ID, info in dictionary.items():
#     if info["Ім`я"] == name:
#         print("Вік людини:", info.get("Вік", "Вік не знайдено"))

# 3
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict3 = {**dict1, **dict2}
# dict3 = dict1.copy()
# for key, value in dict2.items():
#     dict3[key] = value
# print(dict3)

# 4
# for key, value in dictionary.items():
#     if value == 10:
#         print(key)

# 5
# unique_values = set()
# for value in dictionary.values():
#     unique_values.add(value)
# print(len(unique_values))

# 6
# longest_key = ""
# for key in dictionary.keys():
#     key = str(key)
#     if len(key) > len(longest_key):
#         longest_key = key
# print(longest_key)
