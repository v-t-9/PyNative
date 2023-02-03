# https://pynative.com/python-string-exercise/
import string
# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Given:

# str1 = "James" 
# result = str1[0]+ str1[int(len(str1)/2)] +str1[len(str1)-1]
# print(result)

# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
# Given:
# Case 1
# str1 = "JhonDipPeta"
# # Case 2
# str2 = "JaSonAy"
# def midchar(str):

#     result = str[int(len(str)/2)-1] + str[int(len(str)/2)] + str[int(len(str)/2)+1]
#     return  print(result)   
# midchar(str1)
# midchar(str2)

# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# Given:
# s1 = "Ault"
# s2 = "Kelly"
# st1 = " "
# result = ""
# for i in range(0,int(len(s1)/2)):   # pos 0 y 1 de s1
#     st1 = st1 + s1[i]

# result = result + st1 + s2
# for i in range(int(len(s1)/2), len(s1), 1): # pos 2 y 3 de s1
#     result = result + s1[i]

# print(result)

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# Given:
# s1 = "America"
# s2 = "Japan"

# firsts1 = s1[0]
# firsts2 = s2[0]
# middles1 = int(len(s1)/2)
# middles2 = int(len(s2)/2)
# mids1 = s1[middles1]
# mids2 = s2[middles2]
# lasts1 = s1[len(s1)-1]
# lasts2 = s2[len(s2)-1]

# result = firsts1 + firsts2 + mids1 + mids2 + lasts1 + lasts2

# print(result)

# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given: 
# str1 = "PyNaTive"
# lower = []
# upper = []

# for i in str1:
#     if i.islower():
#         lower.append(i)
#     if i.isupper():
#         upper.append(i)

# res = "".join(lower+upper)
# print(res)

# str1 = "PyNaTive"
# lower = ""
# upper = ""
# res=""
# for i in str1:
#     if i.islower():
#         lower = lower + "".join(i)
#     if i.isupper():
#         upper = upper +"".join(i)
# print(lower+upper)

# Exercise 5: Count all letters, digits, and special symbols from a given string
# Given:
# str1 = "P@#yn26at^&i5ve"
# letter =""
# number=""
# countLetter = 0
# countNumber = 0
# countSymbol = 0
# for i in str1:
#     if i.isnumeric():
#         countNumber = countNumber + 1
#     if i.isalpha():
#         countLetter = countLetter +1
# countSymbol = len(str1) - countLetter - countNumber
# print("numeros: ", countNumber)
# print("Letras: ", countLetter)
# print("Simbolos: ", countSymbol)

# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
#  then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# Given:

# s1 = "Abc"
# s2 = "Xyz"
# str2 = s2[::-1]
# str = ""
# length = 0
# if len(s1)>len(s2):
#     length = len(s1)
# else:
#     length = len(s2)

# for i in range(length):
#     str = str + s1[i] + str2[i]

# print(str)

# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced 
# if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
# Given:
# Case 1:
# s1 = "Yn"
# s2 = "PYnative"
# Case 2:
# s1 = "Ynf"
# s2 = "PYnative"
# def balance(str1,str2):
#     for i in str1:
#         if i in str2:
#             return True
#         else:
#             return False
# print(balance(s1,s2))

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?"
# count = 0
# s = str1.lower()
# res = s.count("usa")
# print(res)

# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear 
# in the string, ignoring all other characters.
# Given:
# str1 = "PYnative29@#8496"
# sum = 0
# avg = 0
# count = 0 
# for i in str1:
#     if i.isdigit():
#         sum = sum + int(i)
#         count = count +1

# avg = sum/count

# print("Suma: ",sum, "\nPromedio: ", avg)

# Exercise 10: Write a program to count occurrences of all characters within a string
# Given:
# str1 = "Apple"
# dict = {}
# for i in str1:
#     dict[i] = str1.lower().count(i)
# print(dict)

# Exercise 11: Reverse a given string
# Given: 
# str1 = "PYnative"
# print(str1[::-1])

# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
# Given:
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# pos = str1.rfind("Emma")   # encuentra la ultima ocurrencia de un valor, si no la encuentra devuelve -1
# print(pos)

# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# Given:
# str1 = "Emma-is-a-data-scientist"
# lista1 = []
# lista1 = str1.split("-")
# for i in range(len(lista1)):
#  print(lista1[i])

# Exercise 14: Remove empty strings from a list of strings
# Given:
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# for i in str_list:
#     if not i:
#         str_list.remove(i)
    
# print(str_list)

#Exercise 15: Remove special symbols / punctuation from a string
# Given:
# str1 = "/*Jon is @developer & musician"
# s1 = ""
# s1 = str1.replace("/","")
# s1 = s1.replace("*","")
# s1 = s1.replace("&","") 
# s1 = s1.replace("@","") 
# print(s1)
# str1 = '/*Jon is @developer & musician!!'

# for i in string.punctuation:
#         str1 = str1.replace(i," ")
# print(str1)
# Exercise 16: Removal all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
# str2 = ""
# for i in str1:
#     if i.isnumeric():
#         str2 = str2 + i
# print(str2)

# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
# Given:
# str1 = "Emma25 is Data scientist50 and AI Expert"
# lista= []
# lista = str1.split(" ")
# for i in lista:
#     if i.isalpha() == False:
#         print(i)

# Exercise 18: Replace each special symbol with # in the following string
# Given:
# str1 = '/*Jon is @developer & musician!!'
# for i in string.punctuation:
#         str1 = str1.replace(i,"#")
# print(str1)
