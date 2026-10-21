def promedio_notas(lista, materia):
    acumulado = 0
    longitud = 0
    for alumno in lista:
        if alumno[1] == materia:
            if alumno[2] < 10:
                continue
            else:
                acumulado += alumno[2]
                longitud += 1
        else:
            continue
    if longitud == 0:
        return 0
    else:
        promedio = acumulado / longitud
    return promedio

notas = [
    ('Ana', 'Calculo', 15),
    ('Luis', 'Fisica', 8),
    ('Eva', 'Calculo', 9),
    ('Juan', 'Calculo', 17),
    ('Sofia', 'Fisica', 5),
]

print(promedio_notas(notas, 'Fisica'))