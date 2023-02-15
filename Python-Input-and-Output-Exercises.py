# import os
# Exercise 1: Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication

# n1 = float(input("Ingrese un numero: "))
# n2 = float(input("Ingrese otro numero: "))
# multiplicar = n1 * n2
# print("La multiplicacion es: " , multiplicar)

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.
# Expected Output:
# For example: print('Name', 'Is', 'James') will display Name**Is**James

# print("Name", "Is", "James", sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting

# num = 8
# oct = oct(num)
# stroct = str(oct)
# print(stroct[2:])
# # solucion de la pagina
# print('%o' % num)
# print('Output number in octal format : {0:o}'.format(num))

# Exercise 4: Display float number with 2 decimal places using print()
# num = 458.541315
# print("Numero con 2 decimales : %.2f" % num)

# Exercise 5: Accept a list of 5 float numbers as an input from the user

# numList = []

# for i in range(5):
#     n = float(input("Ingrese un numero decimal: "))
#     num = numList.append(n)

# print("Los numeros ingresados son: {0}" .format (numList))

# Exercise 6: Write all content of a given file into a new file by skipping line number 5
# Create a test.txt file and add the below content to it.

# Given test.txt file:
# line1
# line2
# line3
# line4
# line5
# line6
# line7
# Expected Output: new_file.txt
# line1
# line2
# line3
# line4
# line6
# line7

# text = open("test.txt", "w")
# nuevoContenido = "line1\nline2\nline3\nline4\nline6\nline7"
# text.write(nuevoContenido)
# text.close()

# # ruta absoluta
# nuevoNombre = "new_file.txt"
# viejoNombre = "test.txt"

# os.rename(viejoNombre, nuevoNombre)

# Exercise 7: Accept any three string from one input() call
# Write a program to take three names as input from a user in the single input() function call
# nombre1, nombre2, nombre3 = input("Ingrese 3 nombres ").split()
# print("Los nombres son: {0} , {1}, {2}" .format(nombre1, nombre2, nombre3))

# Exercise 8: Format variables using a string.format() method.
# Write a program to use string.format() method to format the following three variables as per the expected output

# # Given:
# totalMoney = 1000
# quantity = 3
# price = 450
# # d es para int y f para float
# print("Tengo {:.2f} pesos por lo que puedo comprar {:d} pelotas de futbol por {:.2f}".format(totalMoney, quantity, price))

# Exercise 9: Check file is empty or not
# Write a program to check if the given file is empty or not
# tamano = os.path.getsize("new_file.txt")
# if tamano == 0:
#     print("Archivo vacio")
# else:
#     print("Archivo no vacio")

# Exercise 10: Read line number 4 from the following file

# archivo = open("new_file.txt", "r")
# num = 4 #para leer la 4ta linea
# leer = archivo.readlines()
# print(leer[3])
# archivo.close()






    
