A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

suma = []
resta = []

for i in range(3) :
    fila_suma = []
    fila_resta = []
    for j in range(3) :
        elemento_suma = A[i][j] + B[i][j]
        fila_suma.append(elemento_suma)
        elemento_resta = A[i][j] - B[i][j]
        fila_resta.append(elemento_resta)
    suma.append(fila_suma)
    resta.append(fila_resta)
    
print(f'Suma = {suma}')
print(f'Resta = {resta}')