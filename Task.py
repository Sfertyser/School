# Task 1
# dictionary = {
#     "dict1": {'a': 1, 'b': 2},
#     "dict2": {'x': 10, 'y': 20}
# }
# value = dictionary["dict2"]["y"]
# print(value)

# Task 2
# def find_common_elements(dict1, dict2):
#     common_elements = {}
#     for key in dict1.keys():
#         if key in dict2:
#             common_elements[key] = dict1[key]
#     return common_elements
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'c': 4, 'd': 5}
# result = find_common_elements(dict1, dict2)
# print(result)

# Task 3
# Створіть словник, де ключами є кортежі, і напишіть функцію для доступу до значень з використанням кортежів як ключі.
tuple_dict = {
    ('a', 'b'): 1,
    ('x', 'y'): 2
}
key1, key2 = ('a', 'b'), ('x', 'y')
value1, value2 = tuple_dict.get(key1), tuple_dict.get(key2)
print(f"Значення для ключа {key1}: {value1}")
print(f"Значення для ключа {key2}: {value2}")
