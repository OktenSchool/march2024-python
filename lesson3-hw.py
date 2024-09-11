# from typing import Self
# class Rectangle:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#         self.area = self.a * self.b
#
#     def __add__(self, other:Self):
#         return self.area + other.area
#     def __sub__(self, other:Self):
#         return self.area - other.area
#     def __eq__(self, other:Self):
#         return self.area == other.area
#     def __ne__(self, other:Self):
#         return self.area != other.area
#     def __lt__(self, other:Self):
#         return self.area < other.area
#     def __gt__(self, other:Self):
#         return self.area > other.area
#     def __len__(self):
#         return (self.a+self.b)*2
#
#

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Cinderella(Human):
#     __count = 0
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.__count +=1
#     def __str__(self):
#         return str(self.__dict__)
#
#     @classmethod
#     def get_count(cls):
#         print(cls.__count)
#
# class Prince(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#
#     def find_cinderella(self, cinderella_list:list[Cinderella]):
#         for cinderella in cinderella_list:
#             if cinderella.foot_size == self.shoe_size:
#                 print(cinderella)
#                 return
#
# cind_list:list[Cinderella] = [
#     Cinderella('Olha', 25, 32),
#     Cinderella('Kira', 18, 36),
#     Cinderella('Albina', 30, 16),
#     Cinderella('Maria', 25, 15)
# ]
#
# prince = Prince('Max', 15, 36)
# prince.find_cinderella(cind_list)
#
# Cinderella.get_count()


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is book {self.name}')


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is magazine {self.name}')


class Main:
    __printable_list:list[Printable] = []
    @classmethod
    def add(cls, item:Book|Magazine):
        if isinstance(item, (Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('magazine1'))
Main.add(Magazine('magazine4'))
Main.add(Book('book1'))
Main.add(Book('book2'))
Main.add(Magazine('magazine3'))
Main.add(Book('book3'))
Main.add(Magazine('magazine2'))
Main.add(Book('book4'))
Main.add('ddddddddddddddd')

Main.show_all_magazines()
print('********************************************')
Main.show_all_books()
