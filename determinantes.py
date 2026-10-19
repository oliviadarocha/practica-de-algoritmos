#para matrices 2x2

A = [[2,3] , [5,6]]
determinante_2x2 = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

#para matrices nxn por el metodo de cofactores

def obtener_submatriz(matriz, fila_eliminar, col_eliminar): 
    #Primero hay que ir convirtiendo es una 2x2
    #Función auxiliar: Crea una submatriz más pequeña
    #eliminando una fila y una columna específicas.
    
    submatriz = []
    for i in range(len(matriz)):
        if i != fila_eliminar:
            nueva_fila = []
            for j in range(len(matriz[i])):
                if j != col_eliminar:
                    nueva_fila.append(matriz[i][j])
            submatriz.append(nueva_fila)
    return submatriz


def determinante(matriz):
    
    #Función principal: Calcula el determinante de cualquier 
    #matriz cuadrada nxn.
    
    #Caso 1: Matriz de 1x1
    if len(matriz) == 1:
        return matriz[0][0]
    
    #Caso 2: Matriz de 2x2
    if len(matriz) == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    
    # Caso general: por cofactores
    det = 0
    for col in range(len(matriz)):
        # 1. Reducimos la matriz quitando la fila 0 y la columna 'col'
        submatriz = obtener_submatriz(matriz, 0, col)
        
        # 2. Alternamos el signo (+1 o -1) según la posición
        signo = 1 if col % 2 == 0 else -1
        
        # 3. Sumamos acumulando: signo * elemento * determinante(submatriz)
        det += signo * matriz[0][col] * determinante(submatriz)
        
    return det


#Ejemplo de prueba con una matriz 3x3
B = [
    [2, -1, 3],
    [0,  4, 1],
    [1,  5, 2]
]

print("El determinante de la matriz es:", determinante(B))