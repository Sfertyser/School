
password = input('Введіть ваш пароль: ')
(t, y, u, i, o, p) = (0, 0, 0, 0, 0, 0)
s = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
for char in password:
    if len(password) >= 8:
        t = 1
    if char.isdigit:
        y = 1
    if char.isupper:
        u = 1
    if char.islower:
        i = 1
    if any(char in s for char in password):
        o = 1
p = t + y + u + i + o
print(f"Ваша кількість балів: {p}")
if t == 0:
    print("""Ваш пароль складається з менше 8 символів."
    Краще використовувати довші паролі для більшого захисту.""")
if y == 0:
    print("""У Вашому паролі немає чисел.
    Використання чисел в паролі значно підвищує його складність.""")
if u == 0:
    print("""У Вашому паролі немає великих літер.
    Використання великих літер в паролі значно підвищує його складність.""")
if i == 0:
    print("""У Вашому паролі немає маленьких літер.
    Використання маленьких літер в паролі значно підвищує його складність.""")
if o == 0:
    print("""У Вашому паролі немає ніяких знаків.
    Використання знаків в паролі значно підвищує його складність.""")
if p == 5:
    print("Ваш пароль пройшов всі перевірки, ви молодець.")
