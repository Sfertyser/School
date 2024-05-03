"""
1. Шифрування та розшифрування тексту за допомогою шифру Цезаря:
Напишіть функцію для шифрування та розшифрування тексту за допомогою
шифру Цезаря, де ключ - це зміщення літер в алфавіті.
"""


def cesar(text, shift, decrypt=False):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()

    def transform_letter(letter):
        if letter not in alphabet_lower and letter not in alphabet_upper:
            return letter

        new_index = (alphabet_lower.index(letter) + shift) % len(alphabet_lower)
        if decrypt:
            new_index = (new_index - shift) % len(alphabet_lower)

        if letter in alphabet_upper:
            return alphabet_upper[new_index]
        else:
            return alphabet_lower[new_index]

    return "".join([transform_letter(letter) for letter in text])


original_text = "Helloworld"
encrypted_text = cesar(original_text, 3)
print(encrypted_text)
