# https://pynative.com/python-list-exercise-with-solutions/
# Exercise 1: Reverse a list in Python
#Given:
# list1 = [100, 200, 300, 400, 500]
# print(list1[::-1])

# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = []
# l1 = len(list1)
# l2 = len(list2)
# if l1>l2:
#     l = l1
# elif l2>l1: 
#     l = l2
# else:
#     l = l1
# str = ""
# str1=""
# for i in range(0,l):
#         str = str + list1[i] + list2[i] + " "
# str1 = str.strip()
# list3 = str1.split(" ")
# print(list3)

# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# cuadrados = []
# for i in numbers:
#         cuadrados.append(i**2)
# print(cuadrados)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# output = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list3 = []
# l1 = len(list1)
# l2 = len(list2)
# str1 =""
# s1 =""
# element = "Hello"
# for element in list1:
#     for i in range(l2):
#         str1 = str1 + element +list2[i] + " "    

# list3 = str1.split(" ")
# list3.pop()
# list4 = []
# list5 = []
# for i in range(0,len(list3)):
#     if i%2==0:
#         list4.append(list3[i])
#     else:
#         list5.append(list3[i])

# list3[:] = []

# for i in range(0,len(list4)):
#         s1 = s1 + list4[i] + list5[i] + " "
# list3 = s1.split(" ")
# list4[:] = []
# for i in list3:
#   if i.startswith("H"):
#     list4.append(i[:5] + " " + i[5:])
#   if i.startswith("t"):
#     list4.append(i[:4]+ " "+ i[4:])
# print(list4)

# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously 
# and display items from list1 in original order and items from list2 in reverse order.
# Given:
#
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# rev = list2[::-1]
# str1 = ""
# for i in range(len(list1)):
#     for j in range(len(rev)):
#         if i == j:
#             str1 = list1[i] , rev[j]
#             print(str1)

# for i,j in zip(list1,rev):
#     print(i, j)

# list3 = []
# list3 = [i*2 for i in list1 if i>30]
# print(list3)

#Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# remove = ""
# list2 = []
# len = len(list1)
# for i in range(0, len):
#     if list1[i]!="":
#         list2.append(list1[i])

# print(list2)

# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# Given:

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# len = len(list1)
# list1[2][2].append(7000)
# print(list1)

# Exercise 8: Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding 
# the sublist ["h", "i", "j"] in such a way that it will look like the following list.
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence 
# of an item.
# Given:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# pos = []
# for i in range(len(list1)):
#     if list1[i]== 20:
#         pos.append(i)
# list1[pos[0]] = 200
# print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# Given:

# list1 = [5, 20, 15, 20, 25, 50, 20]
# res = []
# len = len(list1)
# for i in list1:
#     if i == 20:
#         list1.remove(i)
# print(list1)




           