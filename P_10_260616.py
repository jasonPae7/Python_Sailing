import os
from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.replace('\n ','')
# print(contents)

# current_path = os.getcwd()
# print(current_path)
# file_path = 'pi_digits'
#
# abs_file_path = os.path.join(current_path, file_path)
# print(abs_file_path)
# if os.path.exists(abs_file_path):
#     with open(abs_file_path, "r") as file:
#         contents = file.read()
#         print(contents)
# else:
#     print("File not exist")

# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I also love working with data.\n"
#
# path = Path('programming.txt')
# path.write_text(contents)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('Division by zero')

#path = Path('C:\\Users\\Jason\\Downloads\\PythonCrashCourse-master\\origin\\chapter_10\\alice.txt')

# def count_words(path):
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print('File not found')
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"This file {path} have {num_words} words.")
#
# filenames = [
# 'C:\\Users\\Jason\\Downloads\\PythonCrashCourse-master\\origin\\chapter_10\\alice.txt'
# ,'C:\\Users\\Jason\\Downloads\\PythonCrashCourse-master\\origin\\chapter_10\\moby_dict.txt'
# ,'C:\\Users\\Jason\\Downloads\\PythonCrashCourse-master\\origin\\chapter_10\\little_women.txt'
# ]
#
# for filename in filenames:
#     path = Path(filename)
#     count_words(path)

import json

def get_stored_username(path):
    if path.exists():
        content =path.read_text()
        username = json.loads(content)
        return username
    else:
        return None

def get_new_username(path):
    username = input(f'Enter your username: ')
    contents = json.dumps(username)
    contents = path.read_text() + ',' + contents
    path.write_text(contents)
    return username

def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        current_username = input("your name? ")
        if current_username in username:
            print(f"Welcome back, {username}!")
        else:
            get_new_username(path)
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back,, {username}!")

greet_user()