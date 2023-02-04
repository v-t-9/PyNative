# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercise 1: Print First 10 natural numbers using while loop
# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1

# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# for i in range(0,6):
#     i = i+1
#     for j in range(1,i):
#         print(j, end= " ")
#     print("\n")

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# num = int(input("Ingrese un numero: "))
# result=0
# for num in range(1,num+1):
#     result= result+num
# print("El  resultado es: ",result)

# Exercise 4: Write a program to print multiplication table of a given number

# num = 2
# for i in range(1,11):
#     result=num*i
#     print(result)

# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if i > 500:
#         break
#     if i > 150:
#         continue
#     if i % 5 == 0:
#         print(i)

# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.
# num = 75869
# str = str(num)
# list = []
# for i in str:
#     list.append(i)
# print(len(list))

# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# for i in range (5,0,-1):
#     for j in range(i,0,-1):
#         print(j , end=" ")
#     print("\n")

# Exercise 8: Print list in reverse order using a loop

# list1 = [10, 20, 30, 40, 50]
# list1.sort(reverse = True)
# print(list1)

# for i in list1:
#     print(i)

# Exercise 9: Display numbers from -10 to -1 using for loop
# for i in range(-10, 0, 1):
#     print(i)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
#  # for permite un else que se ejecuta cuando termina

# for i in range(5):
#     print(i)
# else:
#     print("Done!")

# Exercise 11: Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater 
# than 1 that is not a product of two smaller natural numbers
# Examples:
# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.
# # range
# start = 25
# end = 50
# for i in range(25,50):
#         for j in range(2,i):
#             if (i%j) == 0:
#                 break
#                 # no es primo tiene divisores
#         else:
#             print(i)

# Exercise 12: Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. 
# The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
# numA = 0
# numB = 1
# numList = [numA, numB]
# for i in range(0,8,1):
#         num = numA + numB
#         numList.append(num)
#         numA = numB
#         numB = num
# print(numList)

# Exercise 13: Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# num = 5
# res = 1
# for num in range(num,1,-1):
#     res = res * num
# print(res)

# Exercise 14: Reverse a given integer number. Given:
# num = 76542
# strnum = str(num)[::-1]
# n = int(strnum)
# print(n)
########################################################
# list = []
# strnum = str(num)
# for i in strnum:
#     list.append(i)
#     print(list.sort(reverse = True))
#######################################################
# strnum = str(num)
# str = " "
# len = len(strnum) -1
# for i in range(len, -1, -1): 
#     str = str + strnum[i]
# print(int(str))
######################################################

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(0, len(my_list)):
#     if i%2 != 0:
#      print(my_list[i])

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# Write a program to rint the cube of all numbers from 1 to a given number
# Given:
# input_number = 6
# for i in range(1,input_number+1):
#     print("El numero es ", i , "el cubo es ", i**3)

# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. 
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
# Given:
# # number of terms
# n = 5
# num = "2"
# list = []
# suma = 0
# for i in range(0,n,1):
#     #obtiene la secuencia
#     num2 = num + num * i
#     list.append(num2)
#     #suma
#     num3 = int(list[i])
#     suma = suma + num3
# print(suma)

# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# for i in range(5):
#     print("*"*i)
# for i in range(5,0,-1):
#     print("*"*i)

