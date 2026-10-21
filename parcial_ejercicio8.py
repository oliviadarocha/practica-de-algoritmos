def estudiantes_destacados(registros, nota_corte):
    destacados = []
    for alumnos in registros:
        notas_alumno = alumnos[1]
        promedio = (notas_alumno[0] + notas_alumno[1] + notas_alumno[2]) / 3
        if promedio >= nota_corte:
            nombre = alumnos[0]
            destacados.append((nombre, promedio))
        else:
            promedio = 0
    return destacados

datos = [
    ('Carlos', [18, 15, 12]),   # Promedio: 15.0
    ('María',  [10, 8, 11]),    # Promedio: 9.66
    ('Pedro',  [20, 19, 18])    # Promedio: 19.0
]
nota_destacada = float(input('Ingrese la nota detscada minima: '))
 
print(estudiantes_destacados(datos, nota_destacada))

# Salida esperada para estudiantes_destacados(datos, 14.0):
# [('Carlos', 15.0), ('Pedro', 19.0)]