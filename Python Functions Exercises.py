# https://pynative.com/python-functions-exercise-with-solutions/
# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.
# def nameAge(name, age):
#     return print("Name: ", name, " Age: ", age)
# nameAge("Maria", 24)

#Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.
# Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.
# def func1(*args):
#     #el for es porque args devuelve una tupla
#     for i in args:
#         print(i)

# func1(20,40,60)
# func1(80, 100)

# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# Given:

# def calculation(a, b):
#     suma = a+b
#     resta = a-b
#     return suma, resta
# res = calculation(40, 10)
# print(res)

# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# Given
# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# def showEmployee(nombre, salario = 9000):
#     print("Nombre: ", nombre, " Salario: ", salario)

# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# Exercise 5: Create an inner function to calculate the addition in the following way
# - Create an outer function that will accept two parameters, a and b
# - Create an inner function inside an outer function that will calculate the addition of a and b
# - At last, an outer function will add 5 into addition and return it

# def outer(a,b):
    
#     def inner():
#         return  a + b 
    
#     sum = inner()
#     return sum + 5

# print (outer(2,3))

# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers
# from 0 to 10.

# A recursive function is a function that calls itself again and again.

# def sumNum(num):
#     if num<=1:
#         return 1
#     else: 
#         return num + sumNum(num-1)
       
# print(sumNum(10))

# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) 
# to it and call it using the new name.
# def display_student(name, age):
#     print(name, age)
# # display_student("Emma", 26)
# show_student = display_student
# show_student("Maria", 30)

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# list1 = []
# for i in range(4, 29,2):
#     list1.append(i)
# print(list1)

# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))





