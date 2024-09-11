# try:
#     ksdfkshf
# except NameError as e:
#     print('Error', e)
#
# print('ksdfkshf')
# try:
#     # print(5/0)
#     sdfsdf
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# # except NameError as e:
# #     print(e)
# except Exception as e:
#     print(e)
# finally:
#     print('Finish')


# # print('!!!!!!!!!!!!')
# sum_ = 0
# for i in range(5):
#     sum_+=i


# l = [i for i in range(50_000_000)]
# input()

# g = (i for i in range(50_000_000))
# g = (i for i in range(5))
# print(g)
# # input()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for i in g:
#     print(i)


# def gen(name:str):
#     for ch in name:
#         yield ch
#
#         print('after yield')
#
#
# # print(gen('Max'))
# # print(gen('Max'))
#
# g = gen('Max')
#
# print(next(g))
# print(next(g))
# # print(next(g))
# # print(next(g))


# def gen():
#     yield 1
#     yield 22
#     yield 33
#
#
# g = gen()
#
#
# print(next(g))
# print('code')
# if True:
#     print(next(g))
# print('sdfdsfsdf')
# print('sdfdsfsdf')
# print('sdfdsfsdf')
# print('sdfdsfsdf')
# print(next(g))
# print(next(g))
# from uuid import uuid1
# def gen_file_name():
#     while True:
#         yield f'{uuid1()}.jpg'
#
# g = gen_file_name()
#
# print(next(g))
# print(next(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'return25'
#
#
# g = gen()
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as e:
#     print(e)

# def gen1(n):
#     for i in range(1,n+1):
#         yield f'{i} - Team1'
#
# def gen2(n):
#     for i in range(1,n+1):
#         yield f'{i} - Team2'
#
# teams = [gen2(7),gen1(5)]
#
# while teams:
#     team = teams.pop(0)
#
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass

class MyRange:
    def __init__(self, length):
        self.__length = length
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__length:
            res = self.__counter
            self.__counter += 1
            return res
        raise StopIteration


# my_range = MyRange(5)
# #
# # print(next(my_range))
# # for i in MyRange(5):
# #     print(i)
#
# def my_range(length):
#     counter = 0
#     while counter < length:
#         yield counter
#         counter += 1
#
# for i in my_range(10):
#     print(i)


# file = open('111.txt', mode='r')
# text = file.read()
# file.close()
# print(text)

# try:
#     file = open('111.txt', mode='r')
#     try:
#         text = file.read()
#         print(text)
#     finally:
#         file.close()
# except Exception as e:
#     print(e)

# try:
#     with open('1111.txt') as file:
#         # print(file.read())
#         # print([file.readline()])
#         # print([file.readline()])
#         for line in file:
#             print(line, end='')
# except Exception as e:
#     print(e)


# try:
#     with open('11113.txt', 'r+') as file:
#         pass
#         file.write('Hello world!\n')
#         file.seek(0)
#         print(file.read())
#         file.seek(0)
#         file.write('first\n')
#         # file.write('Hello world2!\n')
# except Exception as e:
#     print(e)

#
# try:
#     with open('11113.txt', 'a') as file:
#         file.write('Hello world!\n')
# except Exception as e:
#     print(e)


import pickle
import json
from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int})

users: list[User] = [
    {'name': 'max', 'age': 15},
    {'name': 'marina', 'age': 20},

]

# try:
#     with open('users.db', 'wb') as f:
#         pickle.dump(users, f)
# except Exception as e:
#     print(e)

# try:
#     with open('users.db','rb') as f:
#         users:list[User] = pickle.load(f)
#         print(users[0]['name'])
# except Exception as e:
#     print(e)


# try:
#     with open('users.json', 'w') as f:
#         json.dump(users, f)
# except Exception as e:
#     print(e)

# try:
#     with open('users.json',) as f:
#         users:list[User] = json.load(f)
#         print(users[0]['name'])
# except Exception as e:
#     print(e)


# num = input('Enter num:')
#
# match num:
#     case '1':
#         print(1)
#     case '2':
#         print(2)
#     case '3':
#         print(3)
#     case _:
#         print('Invalid input')

# l = [1]
# a,= l
# print(a)

act = ['right', '200']
act = ['exit']
act = ['bottom', '200']


# match act:
#     case 'left' as action, value:
#         print(action, value)
#     case 'right' as action, value:
#         print(value)
#     case 'top'|'bottom' as action, value:
#         print(value*200)
#     case 'exit',:
#         print('Exit')


class User:
    __match_args__ = ('name', 'age')

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


user = User('max', 20)

user_dict = {'name': 'Karina', 'age': 33}


# def matcher(source:User|dict):
#     if isinstance(source, User):
#         print(source.name)
#     elif isinstance(source, dict):
#         print(source['age'])
#
# matcher(user_dict)

def matcher(source: User | dict):
    match source:
        case User(name, age=19):
            print(name, '!!!!!!!!!!!!!!!!!!!1')
        case User(name, _):
            print(name)
        case {'age': age}:
            print(age)
        case {'age':33 as age}:
            print(age, '!!!!!!!!!!!!!!')

matcher(user_dict)
