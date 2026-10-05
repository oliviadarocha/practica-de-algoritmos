n = int(input('Ingrese un numero: '))
count = 2
sum = 0

if n > 0 :
    while count < n :
        if (count % 2) == 0 : #solo suma los pares
            sum += count
            count += 1
        else : #los impares se los salta
            count += 1
            continue
    print(sum) 
elif n == 0 :
    print(0)
else :
    print('Ingrese un numero entero positivo.')   
