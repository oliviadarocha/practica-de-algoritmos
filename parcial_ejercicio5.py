def libros_disponibles(b, libro):
    if libro not in b:
        return -1
    else:
        libro = b[libro]
        disponibilidad = libro['ejemplares'] - libro['prestados']
        return disponibilidad
    
biblioteca = {
    'Cien años de soledad': {'ejemplares': 4, 'prestados': 3},
    'El principito': {'ejemplares': 3, 'prestados': 3},
    "Doña Bárbara": {'ejemplares': 5, 'prestados': 2}
}

book = input('Ingrese el nombre del libro: ')
print('libros disponibles:', libros_disponibles(biblioteca, book))