# 6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

def adivinador(): #se crea la funcion para adivinar
    print("Escoja un número del 1 al 100") #se le dice al usuario que piense en un numero

    numero_adivinado = 50 #se define una variable igual a 50
    
    while True: #bucle que siempre se va a ejecutar excepto cuando la respuesta sea "igual"
        respuesta = input(f"{numero_adivinado} es mayor, menor o igual al numero?: ")
        respuesta = respuesta.lower()
        
        if respuesta == "igual": #aqui el bucle se termina
            print(f"El numero es {numero_adivinado}")
            break
        elif respuesta == "menor": 
            numero_adivinado -= 1 #se le resta 1 a la variable y el bucle sigue
        else:    
            numero_adivinado += 1 #se le suma 1 a la variable y el bucle sigue

adivinador() #se llama a la funcion