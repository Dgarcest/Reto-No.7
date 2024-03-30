# 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

n = int(input("Escriba el número: ")) #se le pide al usuario el numero

while n%2 == 0 and n!=0: #el ciclo para cuando n es par y hasta el 2
    print(n)
    n -= 2 #se va restando de 2 en 2

if n%2==1: #condicional por si el numero es impar
    n = n-1 #se convierte el numero en par 
    while n%2==0 and n!=0: #se reutiliza el ciclo
        print(n)
        n -=2