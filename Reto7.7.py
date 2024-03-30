# 7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

numero = int(input("Ingrese un numero del 2 al 50: ")) #se pide el numero

divisor = 1 #se crea una variable igual a 1

print(f"Los divisores de {numero} son:") #print para aclarar el inicio de la lista de los divisores

while divisor<=numero: 
    if numero%divisor == 0: #si el residuo es 0 significa que es divisor
        print(divisor)

    divisor += 1 #incremento para cada iteracion

print(f"Fin lista de los divisores de {numero}") #print para aclarar el fin de la lista de los divisores