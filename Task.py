# Task 1
# words = ["apple", "banana", "grape", "pear", "kiwi", "orange"]
# grouped_by_length = {}
#
# for word in words:
#     lenth = len(word)
#     if lenth in grouped_by_length:
#         grouped_by_length[lenth].append(word)
#     else:
#         grouped_by_length[lenth] = [word]
#
# print(grouped_by_length)

# Task 2
# text_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# text = "three"
# number = text_numbers.get(text, "unknown")
# print(number)

# Task 3
# elements = [1, 2, 3, 2, 1, 3, 1, 2, 4, 5, 1]
# count_dict = {}
# for el in elements:
#     if el in count_dict:
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
# print(count_dict)

# Task 4
# synonyms = {
#     "happy": ["joyful", "content", "pleased"],
#     "sad": ["unhappy", "miserable", "gloomy"],
#     "angry": ["irate", "furious", "enraged"]
# }
# word = "happy"
# end = synonyms.get(word, [])
# print(end)

# Task 5
text = "hello world"
char_count = {}
for t in text:
    if t in char_count:
        char_count[t] += 1
    else:
        char_count[t] = 1
print(char_count)
