# Task 1
text = input("Введіть текст: ")
text2 = ""
for char in text:
    if not char.isdigit():
        text2 += char
print(text2)

# Task 2
email = input("Введіть електронну пошту: ")
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")

# Task 2 optimized
email = input("Введіть електронну пошту: ")
print("YES") if "@" in email and "." in email else print("NO")
