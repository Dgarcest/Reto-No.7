# Reto-No.7

## 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
numero = 1 #se declara la variable

while numero<=100: #ciclo while hasta el numero 100
    cuadrado = numero**2
    print(f"El numero es {numero} y su cuadrado {cuadrado}")
    numero += 1 #se le suma 1 a la variable para que el ciclo no sea infinito
```

## Diagrama de flujo

```mermaid
flowchart TD;
  A[numero = 1] -->B
  B{numero menor
  o igual a 100?} --V--> C
  C[cuadrado = numero**2] ----> D[imprimir el numero
          y el cuadrado]
  D ----> E[numero += 1]
  B --F-->F(Fin)
  E ----> B
```

## 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
```

## Diagrama de flujo

```mermaid
```

## 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
```

## Diagrama de flujo

```mermaid
```

## 4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

```python
```

## 5. Imprimir el factorial de un número natural n dado.

```python
```

## 6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

```python
```

## 7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

```python
```

## 8. Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

```python
```
