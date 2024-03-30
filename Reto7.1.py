# 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado

numero = 1 #se declara la variable

while numero<=100: #ciclo while hasta el numero 100
    cuadrado = numero**2
    print(f"El numero es {numero} y su cuadrado {cuadrado}")
    numero += 1 #se le suma 1 a la variable para que el ciclo no sea infinito