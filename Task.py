#  Класи

# class Cat:
#     def init(self, name, breed):
#         self.name = name
#         self.breed = breed
#
# my_cat = Cat("Павло", "Дворянин")
# print(my_cat.name)

# Наслiдування

# class Animal:
#     def init(self, species):
#         self.species = species
#
# class Cat(Animal):
#     def init(self, name, breed):
#         super().init("Cat")
#         self.name = name
#         self.breed = breed
#
# my_cat = Cat("Павло", "Дворянин")
# print(my_cat.species)

# class Animal:
#     def speak(self):
#         print("Тварина звучить")
#
# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print("Павло мурчить")
#
# my_cat = Cat()
# my_cat.speak()

# Iнкапсуляцiя

# class BankAccount:
#     def init(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#
# my_account = BankAccount(1000)
# my_account.withdraw(100)
# print(my_account.get_balance())

#  Полiморфiзм

# class Cat:
#     def sound(self):
#         print("Мяу")
#
# class Dog:
#     def sound(self):
#         print("Гав")
#
# def make_sound(animal):
#     print(animal.sound())
#
# my_cat = Cat()
# my_dog = Dog()
#
# make_sound(my_cat)
# make_sound(my_dog)

# task 1
# class Student:
#     def __init__(self, name, age, grade):
#         self.__name = name
#         self.__age = age
#         self.__grade = grade
#
#     def name1(self):
#         return self.__name
#
#     def age1(self):
#         return self.__age
#
#     def grade1(self):
#         return self.__grade
#
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Некоректнно заданна оцінка.")
#
#
# student1 = Student("Олександр", 25, 50)
# print(student1.name1())
# print(student1.age1())
# print(student1.grade1())
#
# student1.set_grade(100)
# print(student1.grade1())

# Task 2
