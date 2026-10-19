""""Realice un algoritmo que, dado un número ingresado por el 
usuario, determine si este es:
Primo.
Compuesto.
Oblongo.
Palíndromo.
Perfecto.
Abundante.
Deficiente.
Cuadrado.
Libre de cuadrados."""
"""
PRIMO: Solo divisible entre 1 y sí mismo
• Ejemplos: 2, 3, 5, 7, 11, 13
• El 1 NO es primo

COMPUESTO: Tiene más de dos divisores
• Ejemplos: 4, 6, 8, 9, 10, 12
• Todo número mayor que 1 es primo o compuesto

OBLONGO: Producto de dos números consecutivos (n = k × (k+1))
• Ejemplos: 2=1×2, 6=2×3, 12=3×4, 20=4×5

PALÍNDROMO: Se lee igual de izquierda a derecha que al revés
• Ejemplos: 11, 121, 1331, 12321

PERFECTO: La suma de sus divisores propios es igual al número
• Ejemplos: 6 (1+2+3=6), 28 (1+2+4+7+14=28)

ABUNDANTE: La suma de sus divisores propios es MAYOR que el número
• Ejemplos: 12 (1+2+3+4+6=16 > 12), 18 (1+2+3+6+9=21 > 18)

DEFICIENTE: La suma de sus divisores propios es MENOR que el número
• Ejemplos: 8 (1+2+4=7 < 8), 9 (1+3=4 < 9)

CUADRADO: Es el cuadrado de un número natural (n = k²)
• Ejemplos: 1=1², 4=2², 9=3², 16=4²

LIBRE DE CUADRADOS: No es divisible por ningún cuadrado perfecto > 1
• Ejemplos: 2, 3, 5, 6, 7, 10
• NO libres: 4 (divisible por 4), 8 (divisible por 4), 9 (divisible por 9)
"""
# import math

# def analizar_numero(n):
#     propiedades = []
#     if n > 1:
#         es_primo = True
#         for i in range(2, n):
#             if n % i == 0:
#                 es_primo = False
#                 break
#         if es_primo:
#             propiedades.append("Primo")
#         else:
#             propiedades.append("Compuesto")


#     k = int(math.sqrt(n))

#     if k * (k + 1) == n:
#         propiedades.append("Oblongo") 

#     if str(n) == str(n)[::-1]:
#         propiedades.append("Palíndromo") 


#     suma_div = 0
#     for i in range(1, n):
#         if n % i == 0:
#             suma_div += i     
#     if suma_div == n:
#         propiedades.append("Perfecto")
#     elif suma_div > n:
#         propiedades.append("Abundante")
#     else:
#         propiedades.append("Deficiente")    
    
    
#     if k * k == n:
#         propiedades.append("Cuadrado")  
#     libre = True

#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % (i * i) == 0:
#             libre = False
#             break
#     if libre:
#         propiedades.append("Libre de cuadrados")
#     return propiedades

# num = int(input("Ingrese un número entero positivo: ")) 
# print(f"Resultados para {num}:")
# for p in analizar_numero(num):
#     print("-", p)














"""
Las matrices podrían definirse como distribuciones rectangulares o cuadradas de números o funciones, 
están compuestas por filas y columnas.
Realice un algoritmo que dado un número ingresado por un usuario realice la operación de 
multiplicación de un escalar (número) por la matriz A, el programa deberá mostrar como respuesta 
la matriz resultante de la misma.
matriz A = [[2, 1, 0], [1, 3, 4],  [5, 2, 1]]
Input de ejemplo: 4
Output esperado:
[[8, 4, 0], [4, 12, 16],  [20, 8, 4]]
[A,B,C]
A=[8,4,0]
"""
#def multiplicar_matriz_por_escalar(escalar, matriz):
#    resultado = []
#    for fila in matriz:
#        nueva_fila = []
#        for elemento in fila:
#            nueva_fila.append(elemento * escalar)
#        resultado.append(nueva_fila)
#    return resultado
#
#escalar = int(input("Ingrese un número escalar: "))
#matriz_A = [[2, 1, 0], [1, 3, 4], [5, 2, 1]]
#
#resultado = multiplicar_matriz_por_escalar(escalar, matriz_A)
#
#print("Matriz resultante:")
#print(resultado)
























"""Realice un algoritmo que realice las operaciones de suma y resta entre dos matrices de 3x3 y 
el output del programa devuelva dos matrices, una correspondiente a cada operación.
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]] 
Output:
suma = [[10, 10, 10], [10, 10, 10],  [10, 10, 10]]
resta=  [[-8, -6, -4], [-2, 0, 2],  [4, 6, 8]]
"""
#A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#def sumar_matrices(A, B):
#    a11=A[0][0] + B[0][0]
#    a12=A[0][1] + B[0][1]
#    a13=A[0][2] + B[0][2]
#    a21=A[1][0] + B[1][0]
#    a22=A[1][1] + B[1][1]
#    a23=A[1][2] + B[1][2]
#    a31=A[2][0] + B[2][0]
#    a32=A[2][1] + B[2][1]
#    a33=A[2][2] + B[2][2]
#    return [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]
#
#def restar_matrices(A, B):
#    a11=A[0][0] - B[0][0]
#    a12=A[0][1] - B[0][1]
#    a13=A[0][2] - B[0][2]
#    a21=A[1][0] - B[1][0]
#    a22=A[1][1] - B[1][1]
#    a23=A[1][2] - B[1][2]
#    a31=A[2][0] - B[2][0]
#    a32=A[2][1] - B[2][1]
#    a33=A[2][2] - B[2][2]
#    return [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]
#
#print(sumar_matrices(A, B))
#print(restar_matrices(A, B))





"""
Elabore un programa que dado 20 números generados de forma aleatoria imprima por pantalla 3 listas
1.- Los números pares
2.- Los impares
3.- Los números originales . 
Ayuda: Para generar los números aleatorios importar la función random y usar random.randint para obtener los números y luego almacenar todos los valores en la lista.
"""
#import random
#
#
#def generar_numeros_aleatorios(cantidad, rango_min, rango_max):
#    numeros = []
#    for _ in range(cantidad):
#        numeros.append(random.randint(rango_min, rango_max))
#    return numeros
#
#numeros_aleatorios = generar_numeros_aleatorios(20, 1, 100)
#pares = []
#impares = []
#originales = numeros_aleatorios
#for numero in numeros_aleatorios:
#    if numero % 2 == 0:
#        pares.append(numero)
#    else:
#        impares.append(numero)
#
#print("Números pares:")
#print(pares)
#for numero in pares:
#    print(numero)
#
#print("Números impares:")
#print(impares)
#for numero in impares:
#    print(numero)
#
#print("Números originales:")
#print(originales)
#for numero in originales:
#    print(numero)
