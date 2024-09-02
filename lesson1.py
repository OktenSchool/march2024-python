# import sys
# asd = 5 # lksjdfkjsfkjfj
#
# # kjhsdfkhk
#
# """
# skjfhskjhf
# sljfhksfh
# jshdfkshfjks
# """
#
# '''
# kjshdfkjshdfkjshdfkj
# '''
#
# # jdjjd = 666

# print(1,'222',222, sep='-', end='finish\n')

# i = 3
# f = 1.3
# b = True # False
# s = "text" # 'text'
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# i = str(i)
#
# print()
# print(type(i))
# print(i)

# a=b=c=555
#
# print(a, b, c)


# a = 5

# a++
# ++a
#
# a+=1
# a = a+1

# a = 5
# b = 3
# #
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(round(a/b))
# print(a%b)
# print(a**b)
# # sys.set_int_max_str_digits(1000000000)
# print(2525**2525)

# num = input('Enter number: ')
# print(type(num))
# print('Your number is', num)


# Все пусте це False

# print(a<b)
# print(a<=b)
# print(a>b)
# print(a>=b)
# print(a==b) # print(a is b)
# print(a!=b) # print(a is not b)
#
# st = 'Hello'
#
# print(isinstance(st, int))

# if a<b:
#     kjhsdjfh
#     jhsdfjkh
#     ljsdfj

# # num = input('Enter a number: ')
# #
# # if num =='1':
# #     print('1')
# # elif num =='2':
# #     print('2')
# # else:
# #     print(False)
#
# num = int(input('Enter a number: '))
#
# res = 'yes' if num > 5 else 'no'
#
# print(res)
# # print('yes' if num > 5 else 'no')


# list

# l = [1, 2, 3, 4, 5, 6, 7]

# print(l[3])
# # print(l[33])
# print('hello')
# l[3] = 88
#
# print(l)

# del l[2]
# print(l)
# print(len(l))


# l = [1, 2, 3, 4, 5, 6, 7]

# l2 = l
#
#
#
# l2 = l.copy()
# l[0]=88
#
#
# print(l2)
# print(l)


# l.append(88)
# l.insert(155, 99)
#
# print(l)

# l = [1, 2, 3, 4, 5, 6, 7, 4, 2]
# l2 = [33,444,55,66]

# last = l.pop(2)

# print(last)
# l.remove(45)
# l.extend(l2)
# l3 = l +l2
# print(l3)

# print(l.index(2, 3, 5))
# print(l.index(22))
# l.reverse()
# l.sort()
# l.sort(reverse=True)
# print(l)

# print(l.count(4))
# l.clear()
#
# l = [1, 2, 3, 4, 5, 6, 7, 4, 2]
#
# # new_list =l[::2]
#
# # print(new_list)
# print(l[-2])


# Tuple

# my_tuple = 5,'sss',True
# print(my_tuple[1])
# del my_tuple[2]
# my_tuple[2] = 555
# print(my_tuple)

# dictionary

# dic = {
#     'name':"max",
#     "age":12
# }
# print(dic['aged'])
# print(dic.get('name3', 999))
# print(dic)

# dic.clear()
# dic.copy()

# dict_fromkeys = dict.fromkeys(['name', 'age', 'home'], 555)
# print(dict_fromkeys)

# print(list(dic.items()))
# print(dic.values())
# print(dic.keys())
# pop = dic.pop('name')
# print(pop)
# print(dic)

# popitem = dic.popitem()
# print(popitem)
# print(dic)
# dic = {
#     'name':"max",
#     "age":12
# }
# dic2 = {
#     "home":2
# }
# dic.setdefault("name1", "Karina")
# # dic.update(dic2)
# dic|=dic2
# print(dic)


# # l = [1,2,1,5,6,2,1]
# #
# # s = set(l)
# #
# # print(s)
#
# # s = {1,2,3,1,3,2}
# s = set()
# s.add(5)
# s.add(6)
# s.add(5)
# s.add(7)
# s.add(5)
# # print(type(s))
# print(s)


# set_1 = {1,2,3,4,5, 33}
# set_2 = {4, 33,44}
#
# # print(set_1.issuperset(set_2))
# # print(set_2.issubset(set_1))
# # print(set_1.isdisjoint(set_2))
# # print(set_1.union(set_2))
# # print(set_1.intersection(set_2))
# # print(set_1.difference(set_2))
# # print(set_1.symmetric_difference(set_2))
# # set_1.remove(55)
# # set_1.discard(55)
# pop = set_1.pop()
# print(pop)
# print(set_1)


# strings


# s = """
# jkshdfkjshfkj
# ksfkjshfkjsf
# sdfjhsfh
# """

# print(s)

# st = '*!'*25
#
# print(st)
name = 'Max'
age = 18
weight = 70.5
string = 'Hello, my name is Max, I`m 18 and my weight 70.5 kg'
string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + ' kg'
string = 'Hello, my name is %s, I`m %d and my weight %f kg' % (name, age, weight)
string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)
string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age, name=name, weight=weight)
string = f'hello, my name is {name}, I`m {age} and my weight {weight} kg'


# res = string[0]
# res = string.index('ax')
# res = string.count('a')
# res = string.capitalize()
# res = string.upper()
# res = string.lower()
# res = '111d'.isdigit()
# print('hello world'.title())
# print('Hello world'.swapcase())
# print('Hello world'.startswith('He3'))
# print('Hello world'.endswith('d'))
# print(['   gdgd  '.strip()])
# print(['   gdgd  '.lstrip()])
# print(['   gdgd  '.rstrip()])
# print(['aaa   gdgd  aaa'.strip('a ')])
# print('max-18-2'.split('-'))
# print('max 18 2'.split())
# print('My name is Max'.partition('is'))
# l = ['hello', 'car', 'world']
#
# print('-'.join(l))
# print('hello car world'.replace('l', '__'))
# st = 'hello'
# print(st[:3])
# # print(res)
# print(int('111s'))


# min()
# print(max(3, 4, 5, 1))
# print(max([3, 4, 5, 1]))
# print(sum([3, 4, 5, 1]))
# l = sorted([3, 4, 5, 1], reverse=True)
# i = pow(2, 25)
# print(i)
# print(l)


# def func(a,b,c):
#     print('Hello', a,b,c)
#
# func(5,2,9)


# def func(*args):
#     print('Hello', args)
#
# func(5,2,9)

# def func(a,b,c, d=5, *args, **kwargs):
#     print('Hello', a,b,c, d)
#     print(args)
#     print(kwargs)
#
# func(5,2,9, 88, 88,88,55, name='Max', age=15 )

# dic = {
#     "name":"Max",
#     "age":18
# }
#
# def func(name, age):
#     print(name, age)
#
#
# l = [1,2]
#
# func(**dic)

#
# i = 5
# while i>0:
#     i-=1
#     if i ==2:
#         continue
#     print(i)
# else:
#     print('end while')


# l = [1,4,8,1,3]
#
# for i, value in enumerate(l):
#     print(i)
#     print(value)
# else:
#     print('end')


# for i in range(2, 20, 2):
#     print(i)

# dic = {
#     "name":"Max",
#     "age":18
# }
#
# for k,v in dic.items():
#     print(f'{k=}: {v=}')


# list comprehension

l = [1,2,3,4,5]

# l =[i for i in range(10)]
# print(l)

# print([i**2 for i in l])
# print([i for i in l if i%2==0])
# print([i**2 for i in l if i%2==0])
# print(['even' if i %2==0 else 'odd' for i in l])

dict1 = {"Name":'Vasia', "agE":18}

res = {k.lower():v for k,v in dict1.items()}

print(res)