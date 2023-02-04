# https://pynative.com/python-dictionary-exercise-with-solutions/
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict = {}
# len = len(keys)
# for i in range(len):
#     dict.update({keys[i] : values[i]})
# print(dict)

# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)
##########################################
# dict_res = {}
# dict_res.update(dict1)
# dict_res.update(dict2)
# print(dict_res)
###########################################
# dict_res = {**dict1, **dict2}
# print(dict_res)

# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# res = sampleDict["class"]["student"]["marks"]["history"]
# print(res)

# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.
# Given:

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# # fromkeys() devuelve un diccionario con las llaves y valores especificados
# res = dict.fromkeys(employees, defaults)

# print(res)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# Keys to extract
# keys = ["name", "salary"]
# res = dict(filter(lambda key: key[0] in keys, sample_dict.keys()))
# res = {}
# for i in keys:

#     res.update({i:sample_dict[i]})
         
# print(res)

# Exercise 7: Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
# Write a Python program to check if value 200 exists in the following dictionary.
# Given:

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# for i in sample_dict:
#  if sample_dict[i] == 200:
#     print(200, " existe en el diccionario")

# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

# Given:

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# keys = sample_dict.keys()
# if "city" in keys:
#     sample_dict.update({"location": sample_dict["city"]})
#     sample_dict.pop("city")
# print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# min = min(sample_dict)
# print(min)

# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
# Given:
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }

# sample_dict["emp3"]["salary"] = 8500

# print(sample_dict)