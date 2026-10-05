n = int(input('Ingrese un numero: '))
count = 2
sum = 0

if n > 0 :
    while count < n :
        if (count % 2) == 0 :
            sum += count
            count += 1
        else :
            count += 1
            continue
    print(sum) 
elif n == 0 :
    print(0)
else :
    print('Ingrese un numero entero positivo.')   
