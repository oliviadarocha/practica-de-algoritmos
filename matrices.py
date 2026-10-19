n = int(input('Ingrese un numero entero: '))
A = [[2, 1, 0], [1, 3, 4],  [5, 2, 1]]

# B = []
# for fila in A :
#     fila_B = []
#     for elemento in fila :
#         elemento_nuevo = elemento * n
#         fila_B.append(elemento_nuevo)
#     B.append(fila_B)
 
B = [[elemento * n for elemento in fila] for fila in A] #otra forma de hacerlo con python
    
print(B)