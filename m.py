#1
# import my_module as m
# m

#2
# from random import choice
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = []
# for i in range(4):
#     random_names.append(choice(names))
# print(random_names)

#3
# import sys
# print(sys.platform)

#4
# i = input('agruments: ')
# def print_args(a):
#     print(eval(a))
# print_args(i)

#5
# from os import system
# from random import randint
# need_path = '/home/adil/Desktop/'
# direc_name = 'random_files/'
# path = need_path+direc_name
# for i in range(5):
#     r = randint(1,10)
#     system(f'mkdir {path}')
#     system(f'touch {path}{r}.txt')


#6
# from random import shuffle
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

# shuffle(names)
# t1 = names[:3]
# t2 = names[3:6]
# t3 = names[6:9]
# t4 = names[9:]
# print(t1,t2,t3,t4)

#7
# import sys
# sys.args = eval(input('argum: '))
# print(sys.args)

#8
# import sys 
# n1 = int(input('num1: '))
# n2 = int(input('num2: '))
# print(sys.getsizeof(n1))
# print(sys.getsizeof(n2))

#9
# from random import choice

# i = int(input('len of password: '))
# def generate_password(num):
#     symbols = '1234567890qwertyuioasdfghjklzxcvbnm@#$%*&'
#     password = ''
#     for i in range(num):
#         password+=choice(symbols)
#     return password
# print(generate_password(i))

#10

#from random import choice
#i = input('камень, ножницы бумага: ')
#def play(ch):
#     bot_choices = choice(['камень',"ножницы","бумага"])
#     user = ch
#     if user == bot_choices:
#         return 'Draw'
#     elif user == 'камень':
#         if bot_choices == 'ножницы':
#             return f'Победили вы!!!, {user}'
#         else:
#             return f"Победил бот, {bot_choices}"
#     elif user == 'бумага':
#         if bot_choices == 'камень':
#             return f'Победили вы!!!, {user}'
#         else:
#             return f"Победил бот, {bot_choices}"
#     elif user == 'ножницы':
#         if bot_choices == 'бумага':
#             return f'Победили вы!!!, {user}'
#         else:
#             return f'Победил бот, {bot_choices}'
    
#     else:
#         return 'NOT CORRECT NAME!!!' 
# print(play(i))

#11
# from random import randrange
# a = randrange(6,12,2)
# b = randrange(5,100,5)
# print(f'n1: {a}, n2: {b}')


#12
# import os
# import sys

#OS
# cwd = os.getcwd()
# print(cwd)

# path = '/home/adil/Desktop/Folder_Ex'

# # os.mkdir(path)
# # print('Directory is created')

# os.rmdir(path)
# print('directory is removed')

#SYS
# print(sys.version)

# sys.stdout.write('hello \n')

# print(sys.path)

#13
# import datetime

# today = datetime.datetime.now()
# after_1000_days = datetime.timedelta(days=1000)
# final = today + after_1000_days
# print(final)


#ПОВТОРЕНИЕ

#1

# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# sum_numbers_prev_next = [numbers[i]+numbers[i-1] for i in range(1,len(numbers))]
# print(sum_numbers_prev_next)

#2
# from datetime import datetime
# print(datetime.now())

#3
# import time
# for i in range(10):
#     print()
#     time.sleep(0.6)


#4
# list1 = [1,3,5,7,9,11,13]

# list2 = [2,4,6,8,10,12,14]

# zipped = zip(list1,list2)
# for i,j in zipped:
#     print(i,j)





