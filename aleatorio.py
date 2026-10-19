import random

numeros = []
pares = []
impares = []

for n in range(20):
    aleatorio = random.randint(1, 100)
    numeros.append(aleatorio)
    
for n in numeros :
    if n % 2 == 0 :
        pares.append(n)
    else :
        impares.append(n)
    
print(f'Original = {numeros}')
print(f'Pares = {pares}')
print(f'Impares = {impares}')