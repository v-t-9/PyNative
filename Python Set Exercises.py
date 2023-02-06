# https://pynative.com/python-set-exercise-with-solutions/

# Exercise 1: Add a list of elements to a set
# Given a Python list, Write a program to add all its elements into a given set.
# Given:
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]

# sample_set.update(sample_list)
# print(sample_set)

# Exercise 2: Return a new set of identical items from two sets
# Given:
# set1 = {10, 20, 30, 40, 50}            # en los conjuntos se usan las operaciones de union, interseccion, diferencia y diferencia simetrica.
# set2 = {30, 40, 50, 60, 70}
# set3 = set()
# set3 = set1 & set2
# print(set3)

# Exercise 3: Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.symmetric_difference(set2)
# print(set3)

# Exercise 4: Update the first set with items that don’t exist in the second set
# Given two Python sets, write a Python program to update the first set with items 
# that exist only in the first set and not in the second set.

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set1.difference_update(set2)
# print(set1)

# Exercise 5: Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.

# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {10, 20, 30}
# set1.difference_update(set2)
# print(set1)

# Exercise 6: Return a set of elements present in Set A or B, but not both
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.symmetric_difference(set2)
# print(set3)

# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# if set1.intersection(set2) != None:
#     print(set1.intersection(set2))

# Exercise 8: Update set1 by adding items from set2, except common items
# Given:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1.symmetric_difference_update(set2)
# print(set1)

# Exercise 9: Remove items from set1 that are not common to both set1 and set2
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1.intersection_update(set2)
# print(set1)