# import time
# tuple1 = (1, 2)
#
# a, b = tuple1
#
# print(a,b)

# a = 6
# b = 10
#
# b,a = a,b
#
# print(a, b)
#
# l = [1,2,3,4,54,23,44]
#
# # a,b, *_ = l
# a,_,b,*_,c,d = l
#
# print(a, b, c, d)
# def decor(func):
#     def inner(*args,**kwargs):
#         print('*****************************')
#         func(*args, **kwargs)
#         print('*****************************')
#     return inner
# def decor1(func):
#     def inner(*args,**kwargs):
#         print('----------------------------')
#         func(*args, **kwargs)
#         print('----------------------------')
#     return inner
# @decor1
# @decor
# def greeting(name, age):
#     print(f"Hello, {name} {age=}")
#
# greeting("max", 15)

# # f = decor(greeting)
# # f("Max", 18)


# def decor(func):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         print('Time:',time.time() - start_time)
#     return inner
# @decor
# def fun():
#     for i in range(150_000_000):
#         pass
#
#
# fun()
# def func():
#     pass
# name = 'max'
#
# for i in range(5):
#     print(i)
#     # print(globals())
#
# print(i)

# print(globals())

# name = 'Kiril'
# def a():
#     global name
#     age = 5
#     name = "max"
#     print(name)
#     print(locals())
#
# a()
# print(name)
# # print(globals())

# name = 'max'
# def a():
#     name = 'kiril'
#     def b():
#         nonlocal name
#         name = 'Marina'
#         print(name)
#     b()
#     print(name)
#
#
# a()
# print(name)


# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
#
#
# counter1 = counter()
# counter2 = counter()
#
# print(counter1())
# print(counter2())
# print(counter2())
# print(counter2())
# print(counter1())
# print(counter2())


# const func = (a,b)=>a+b

# func = lambda a,b: a+b
#
# print(func(5,5))

# users = [
#     {"name":'max', 'age':15},
#     {"name":'masha', 'age':20},
#     {"name":'Karina', 'age':16},
#     {"name":'Anton', 'age':10},
# ]
#
# users.sort(key=lambda item:item['age'], reverse=True)
#
# print(users)

# l = [1,2,3,4,5]
#
# # map1 = map(lambda i: i ** 2, l)
# #
# # for i in map1:
# #     print(i)
# # for i in map1:
# #     print(i)
#
# f = filter(lambda x: x % 2 == 0, l)
# for i in f:
#     print(i)

# import time
# from time import time
# print(time())

MyType = int | bool

from typing import List, Dict, Tuple, Any, Callable, NewType, TypedDict

# def asd(name:list[str]):
# # def asd(name:tuple[str, list[str], bool])->MyType:
# def asd(name:tuple[str, ...])->Any:
#     print(name)
#     return True
#
# asd(('1', '[1,2]'))
#
# def counter()->Callable[[str, bool], int]:
#     count = 0
#
#     def inner(a:str, b:bool)->int:
#         nonlocal count
#         count+=1
#         return count
#     return inner


# UserId = NewType('UserId', int)
#
# def func(user_id:UserId):
#     print(user_id)
#
# func(UserId(111))


User = TypedDict('User', {
    'id': int,
    'name': str,
    'age': int,
    'house': int
}, total=False)

# user: User = {'id': 15, 'name': 'Max', 'age': 22, 'house': 25}
user: User = {'id': 15, 'name': 'Max', 'asd': 22}
user: User = {}
