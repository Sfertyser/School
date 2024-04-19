class Person:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Company: {self.company}")

    def __del__(self):
        print("Видалено людину з ім'ям:", self.name)


artem = Person("Артем", 14, "Google")
print(artem.name)
print(artem.age)
print(artem.company)
artem.age = 15
print(artem.age)
artem.display_info()
sergiy = Person("Сергій", 15, "Microsoft")
print(sergiy.name)
print(sergiy.age)
sergiy.company = "Samsung"
print(sergiy.company)
sergiy.display_info()
andriy = Person("Андрій", 16, "Amazon")

# class Hello:
#     def say_hello(self, message):
#         print(message)
#
#
# artem = Hello()
# artem.say_hello("hello")
