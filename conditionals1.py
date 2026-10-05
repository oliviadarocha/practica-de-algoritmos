n = int(input('Ingres los puntos que tiene: '))

if (1 <= n) and (n <= 50) :
    print(f"No hay premios para {n} pts")
elif (51 <= n) and (n <= 150) :
    print(f'Felicitaciones, Ganaste la medalla de Bronze por haber tenido {n} pts!')
elif (151 <= n) and (180 <= n) :
    print(f'Felicitaciones, Ganaste la medalla de Plata por haber tenido {n} pts!')
elif (181 <= n) and (n <= 200) :
    print(f'Felicitaciones, Ganaste la medalla de Oro por haber tenido {n} pts!')