
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
    print("Ваш пароль складається з менше 8 символів ")
if y == 0:
    print("Цифри")
if u == 0:
    print("Великі літери")
if i == 0:
    print("Маленькі літери")
if o == 0:
    print("Знаки")
if p == 5:
    print("Все правильно")
