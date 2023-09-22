# task 1 version 1
# def final_words(first_words):
#     dictionary_words = {}
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         if sorted_letters in dictionary_words:
#             dictionary_words[sorted_letters].append(word)
#         else:
#             dictionary_words[sorted_letters] = [word]
#     return dictionary_words
#
#
# first_words = ["риба", "школа", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")

# task 1 version 2
# from collections import default-dict
# def final_words(first_words):
#     anagram_groups = default-dict(list)
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         anagram_groups[sorted_letters].append(word)
#     return dict(anagram_groups)
#
#
# first_words = ["риба", "школа", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")

# task 2
# Напишіть функцію, яка приймає математичний вираз у вигляді рядка (наприклад, "2 + 3 * 4") і обчислює його результат.
def math(examples):
    stack = []
    operators = set(["+", "-", "*", "/"])
    for char in examples:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == "+":
                results = operand1 + operand2
            elif char == "-":
                results = operand1 - operand2
            elif char == "*":
                results = operand1 * operand2
            elif char == "/":
                results = operand1 / operand2
            stack.append(results)
    return stack[0]


examples = "2 + 3 * 4"
result = math(examples)

print(result)
