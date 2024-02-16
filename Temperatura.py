# Ejercicio NO.2 programa para convertir una cantidad grados c a su equivalent a K y F

# imput

C = input("Digite la cantidad de grados C a convertir: ")
C = int(C)

# Processing 

F= (C * (9/5)) + 32
K= C + 273.15

#Output

print ("Grado Fahrenheit: " + str(F))
print ("Grados kelvin: " + str(K))
