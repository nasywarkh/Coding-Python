# -*- coding: utf-8 -*-
"""Project-Dict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D8wLvyW--qMsZ1BXUxWFPw7lU_t833W_
"""

name = input("Enter the name of your favorite hobby :")
function_hobby = input("Enter the function of your favorite hobby :")

hobby_dict = dict(name=name, function=function_hobby)

print("Dictionary for favorite food")
print(hobby_dict)

hobby_dict['year'] = 2023
hobby_dict['place'] = 'Home'

print('update dictionary')
print(hobby_dict)