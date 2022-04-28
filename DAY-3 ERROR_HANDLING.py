'''
Date: 20th April 2022 Wednesday 
Name: kavuri venkatesh reddy
File Desc: Error Handling
'''
# print("Python")
# print("Core Python")
# try:
#     print(5/0)
# except: 
#     print('you have divided by zero')
# print("Advance Python")
# print("Python Analytics")

''' part-2'''
# print("Python")
# print("Core Python")
# try:
#     print(10/5)
# except: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-3 """
# print("Python")
# print("Core Python")
# a=5
# try:
#     print(b)
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" part-4"""
# print("Python")
# print("Core Python")
# a=5
# try:
#     print(a/5)
#     print(b)
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-5"""
# print("Python")
# print("Core Python")
# a=5
# try:
#     print(a/5)
#     print(a/0)
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-6"""
# print("Python")
# print("Core Python")
# a=5
# try:
#     print(a/5)
#     print(b)
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# except NameError:
#     print('You have not defined the name')
# print("Advance Python")
# print("Python Analytics")

""" Part-7"""
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a)
#     print(a/0)
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-8"""
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a/0)
#     print("Hello")
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-9"""
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a/0)
#     print(a+a)
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-10"""
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a/0)
#     print(b+"Hello")   
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-11"""
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     # print(a/0)
#     print(,)   
# except SyntaxError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

""" Part-12 """
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)  
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# finally:
#     print("Its ok next time don't divide by zero")   
# print("Advance Python")
# print("Python Analytics")

""" Part-13 """
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a/0)  
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# finally:
#     print("Its ok next time don't divide by zero")   
# print("Advance Python")
# print("Python Analytics")

""" Part-14"""
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a/0)  
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# else:
#     print("Its ok next time don't divide by zero")   
# print("Advance Python")
# print("Python Analytics")


""" AssertionError"""
# n=int(input('Enter any value:'))
# if n<17:
#     assert print("You are not eligible to vote")

# v=int(input('Enter any value:'))
# if (v<18):
#     raise print('Its possible')

""" Making your own errors with exception"""
# n=201
# if (n>40):
#     raise Exception('The value entered more than 40')