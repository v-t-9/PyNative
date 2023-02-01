# https://pynative.com/python-basic-exercise-for-beginners/

# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, 
# else return their sum.

# num1 = int(input("Ingrese numero 1: "))
# num2 = int(input("Ingrese numero 2: "))

# if num1 * num2 <= 1000:
#     print("El resultado es: ", num1 * num2)
# else:
#     print("El resultado es: ", num1 + num2)

# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

# for i in range(0,10,1):
#    if i == 0:
#         print("El numero anterior es ", i, ". El numero actual es " , i, ".La suma es " , i)
#    else:
#     numAnterior=i-1
#     print("El numero anterior es ", numAnterior, ". El numero actual es " , i, ".La suma es " , (numAnterior + i))
   
# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# str = "pynative"

# for i in range(len(str)):
#     if i % 2 == 0:
#         print(str[i])

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
# For example:
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.

# def remove(st, num):
#     str1 = st[num:]
#     print(str1)

# remove("pynative",4)

# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def first_and_last(list):
#     l = len(list)-1
#     if list[0] == list[l]:                    #tambien pudo haber sido list[-1] para acceder al 'ultimo elemento de la lista
#         return True
#     else:
#         return False

# print(first_and_last(numbers_x))
# print(first_and_last(numbers_y))

# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5
# Given list is  [10, 20, 33, 46, 55]
# list = [10, 20, 33, 46, 55]
# print("Numeros divisibles por 5: ")
# for i in list:
#     if i%5==0:
#         print(i)
# 
# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.
# str_x = "Emma is good developer. Emma is a writer"
# word = "Emma"
# def count_substring(string, w):
#     return string.count(w)

# print(count_substring(str_x, word))

# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(i):
#         print(i, end=" ")
#     print("\n")

# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. 
# For example 545, is a palindrome number.
# num = "121"                                    #devuelve el string dado vuelta [::-1]
# if num == num[::-1]:
#     print("El numero ", num, "es capicua")
# else:
#     print("El numero ", num, "no es capicua")

# Exercise 10: Create a new list from a two list using the following condition
# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that 
# the new list should contain odd numbers from the first list and even numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# def odd_and_even(list1, list2):
#     list3=[]
#     for i in list1:
#         if i % 2 != 0:
#             list3.append(i)
#     for i in list2:
#         if i % 2 == 0:
#             list3.append(i)
    
#     return list3

# print(odd_and_even(list1, list2))

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits

# num=7536
# n=str(num)
# cadena=n[::-1]
# num2=" "
# resultado = " "
# for i in cadena:
#  resultado = resultado + num2.join(i) + num2.join(" ")
# print("Resultado: ",resultado)

# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	        0
# Next $10,000	        10
# The remaining	        20

# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

# ingreso = 45000
# impuesto = 0
# if ingreso >= 0:
#         impuesto = impuesto + (ingreso*0)
#         ingreso = ingreso - 10000
#         if ingreso > 10000:
#             impuesto = impuesto + (10000*0.1)
#             ingreso = ingreso - 10000
#             if ingreso > 20000:
#                 impuesto = impuesto + (ingreso*0.2)
#                 ingreso = ingreso - 10000
# print("El impuesto es: ",impuesto)

# Exercise 13: Print multiplication table form 1 to 10
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end=" ")
#     print("\n")

# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# for i in range(6,1,-1):
#     for j in range(1, i, 1):
#         print("*", end=" ")
#     print("\n")

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises
#  to the power of exp.

# def exponent(base, exp):
#     result = base ** exp
#     return result

# print(exponent(5,4))

    

