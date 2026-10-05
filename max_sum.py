a = float(input('Ingrese un numero a: '))
b = float(input('Ingrese un numero b: '))
c = float(input('Ingrese un numero c: '))

if (a <= b) and (a <= c) :
    print(b + c)
elif (b <= c) and (b <= a) :
    print(a + c)
else :
    print(a +b)