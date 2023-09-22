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
# first_words = ["риба", "школа", "дім", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")

# task 1 version 2
# from collections import defaultdict
# def final_words(first_words):
#     anagram_groups = defaultdict(list)
#     for word in first_words:
#         sorted_letters = "".join(sorted(word))
#         anagram_groups[sorted_letters].append(word)
#     return dict(anagram_groups)
#
#
# first_words = ["риба", "школа", "дім", "магазин", "хімія", "біологія", "літак", "зошит", "офіс", "фабрика", "бар", "раб"]
# anagrams = final_words(first_words)
#
# for key, value in anagrams.items():
#     print(f"Анаграмна група {key}: {value}")


