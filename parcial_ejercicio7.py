def asistencia_taller(agenda, persona):
    inscripciones = []
    for cursos in agenda:
        taller = agenda[cursos]
        if persona in taller:
            inscripciones.append(cursos)
        else:
            continue
    return inscripciones

talleres = {
    'Programación': ['Ana', 'Juan', 'Luis'],
    'Diseño': ['Eva', 'Ana', 'Sofia'],
    'Robótica': ['Juan', 'Luis']
}
nombre = input('Ingrese su nombre: ')

print('Esta inscrito en:', asistencia_taller(talleres, nombre))

# Salida esperada para asistencia_taller(talleres, 'Ana'):
# ['Programación', 'Diseño']