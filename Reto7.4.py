"""
4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. 
Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
"""
#se declaran las 3 variables
pais_a = 25000000 
pais_b = 18900000
fecha = 2022

while pais_b<pais_a: #ciclo cuando la población del B es menor
    print(f"En el año {fecha} la poblacion del pais A es {pais_a}, la del pais B es {pais_b}") #se imprime el incremento cada año
    #se incrementa cada año la población con la tasa de crecimiento
    pais_a = pais_a + pais_a*(2/100) 
    pais_b = pais_b + pais_b*(3/100) 
    fecha += 1

#cuando el ciclo terminó significa que el B supero al de A y se imprime el mensaje
print(f"La poblacion del pais A de {pais_a} habitantes fue superada por el pais B con una poblacion de {pais_b} en el año {fecha}")