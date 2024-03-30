# 8. Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

def primo(numero): #funcion para saber si el numero es primo o no
    numero_divisor = 1 #se define una variable = 1 que es el divisor
    indicador = 0 #se define una variable por si el numero tiene mas de 2 divisores, que al inicio es 0
    while numero_divisor<=100: 
        if numero%numero_divisor == 0: #si es cierto significa que numero_divisor es divisor de numero
            indicador += 1 #el numero de veces que aumente significa el numero de divisores que tiene el numero
            if indicador > 2: #si es cierto significa que el numero no es primo ya que tiene mas de 2 divisores, entonces retorna un False
                return False
        numero_divisor += 1 #se incrementa el divisor en 1 y se vuelve a el ciclo
    return True #si se salio del bucle significa que no retorno un Falso nunca, osea no tiene mas de 2 divisores por lo que es primo y se retorna un True

if __name__ == "__main__": #funcion main
    numero = 2 #variable = 2 ya que 1 no es primo
    while numero<=100: 
        if primo(numero) == True: #si el numero es primo
            print(f"{numero} es primo")
        numero +=1 #incremento cada ciclo