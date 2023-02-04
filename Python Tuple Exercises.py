# https://pynative.com/python-tuple-exercise-with-solutions/

# Exercise 1: Reverse the tuple
# Given:
# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[::-1])

# Exercise 2: Access value 20 from the tuple
# The given tuple is a nested tuple. write a Python program to print the value 20.
# Given:
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# value = tuple1[1][1]
# print(value)

# Exercise 3: Create a tuple with single item 50

# t1 = (50,)
# print(t1)

# Exercise 4: Unpack the tuple into 4 variables
# Write a program to unpack the following tuple into four variables and display each variable.
# Given:
# tuple1 = (10, 20, 30, 40)
# a = tuple1[0]
# b = tuple1[1]
# c = tuple1[2]
# d = tuple1[3]
# print(a)
# print(b)
# print(c)
# print(d)
# Exercise 5: Swap two tuples in Python
# Given:
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# list1 = list(tuple1)
# list2 = list(tuple2)
# tuple1 = (list2)
# tuple2 = (list1)
# print(tuple1)
# print(tuple2)
# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple 
# into a new tuple.
# Given:
# tuple1 = (11, 22, 33, 44, 55, 66)
# list1 = []
# tuple2 = ()
# for i in range(len(tuple1)):
#     if tuple1[i] == 44 or tuple1[i] == 55:
#         list1.append(tuple1[i])
# tuple2 = tuple(list1)
# print(tuple2)

# Exercise 7: Modify the tuple
# Given is a nested tuple. Write a program to modify the first item (22) of a list 
# inside a following tuple to 222
# Given:
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)

# Exercise 8: Sort a tuple of tuples by 2nd item
# # Given:
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# # key establece el elemento por el que se va a ordenar.
# t2 = sorted(tuple1,key = lambda x: x[1])
# print(t2)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple
# Given:
# tuple1 = (50, 10, 60, 70, 50)
# c = tuple1.count(50)
# print(c)

# Exercise 10: Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)

# print(all( i == tuple1[0] for i in tuple1))
