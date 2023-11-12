# f = open("new_file.txt", "x")
# f.close()

# f = open("new_file.txt", "r")
# print(f.read(5))
# f.close()

# f = open("new_file.txt", "a")
# print(f.write("\n hello,world"))
# f.close()

# with open('new_file.txt', 'r') as f:
#     print(f.read())
# with open('new.txt', 'bx') as f:
#     pass
# with open('new.txt', 'bw') as f:
#     f.write(b'some text')

# with open('newf.txt','r') as f:
#     print(f.readlines())
    
# import os
# path = '/Users/baqarichumburidze/Desktop/იტ/python/myself/class'
# a = os.listdir(path)
# print(a)
# for i in a:
#     if i [-2:]
# from random import choice
# file = open('first.txt', 'x')
# file.close()

# with open('les.txt', 'r+') as f:
#     for i in range(randint(10,20)):
#         f.write('text1\n')
# def file_length(f_name):
#     with open (f_name) as f:
#         for i,line in enumerate(f):
#             pass
#     return i+1

# file_length('les.txt')
# from random import randint
 
# with open("first.txt", "r+") as file:
#     for i in range(randint(10, 20)):
#         file.write("something\n")

# def file_length(f_name):
#     with open(f_name) as f:
#         for i, line in enumerate(f):
#             pass
#     return i+1
# print(file_length("first.txt"))

# def text_to_list(f_name):
#     llist = []
#     with open(f_name) as f:
#         for line in f:
#             llist.append(line)
#     print(llist)
# text_to_list('les.txt')

# def random_line(f_name):
#     with open (f_name) as file:
#         lines = file.read().splitlines()
        
#         return choice(lines)
# print(random_line('les.txt'))

# f = open('les.txt')
# print(f.closed)
# f.close()
# print(f.closed)

# def word_counter(f_name):
#     with open(f_name) as file:
#         data = file.read()
#         data.replace(',',' ')
#     return len(data.split(' '))
# print(word_counter('les.txt'))

# f = open('les.txt')
# f.seek(2)
# print(f.readline())
# f.close()

# import shutil
# src = "/Users/baqarichumburidze/Desktop/source_files"
# dst = "/Users/baqarichumburidze/Desktop/destination_files/aall"

# shutil.copytree(src=src, dst=dst)


import shutil

while True:
    choice = input("""
    choose:
    1.copy all files and folders in new folder
    2.Remove folder 
    3.end                   
    """)
    if choice == '3':
        print('task ended')
        break
    elif choice == '1':
        src = input('enter source: ')
        dsc = input('enter destenetion: ' )+ '/just_created'
        try:
            shutil.copytree(src=src,dst=dsc)
        except:
            print('try was not successful')
    elif choice == '2':
        src = input('enter path of the file delete')
        try:
            shutil.rmtree(src)
        except:
            print('try was not successful')


