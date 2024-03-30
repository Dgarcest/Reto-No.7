# 5. Imprimir el factorial de un número natural n dado.

n = int(input("Escriba el numero al que le quiere sacar el factorial: ")) #se pide al usuario el numero

#se tiene en cuenta el caso en el que el numero sea 1
if n==1:
    print("El factorial de 1 es 1")

#se declara una variable la cual va a ser la multiplicación del numero con el numero anterior
p = n * (n-1)

while n>2: #ciclo mientras cuando el numero es mayor a 2
    n -= 1 #se disminuye en 1 el numero
    p = p * (n-1) #el p ya declarado se multiplica con el anterior del numero anterior, ya que en este punto se disminuyo n en 2 por la linea de arriba

#se pone el if por si el numero es 1 para que no imprima la linea
if n!=1:
    print(f"El factorial es {p}")