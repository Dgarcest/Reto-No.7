# 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

numero = 1 #se declara la variable impar

while numero<=999: 
    print(numero)
    numero += 2 #se le suma de 2 en 2 al impar inicial de forma que imprime solo los impares

print("Fin listado números impares") #aclaracion para separar los listados

numero = 0 #se re-declara la variable pero esta vez con un par

while numero<=1000:
    print(numero)
    numero += 2 #se le suma de 2 en 2 al par re-declarado de forma que imprime solo los pares

print("Fin listado números pares") #aclaracion para separar los listados