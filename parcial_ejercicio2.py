def camino_recorrido(camino):
    x = 0
    y = 0
    visitados = [(x, y)]
    for paso in camino :
        if paso == 'N':
            y += 1
        elif paso == 'S':
            y -= 1
        elif paso == 'E':
            x += 1
        elif paso == 'W':
            x -= 1
        if (x, y) in visitados:
            return True
        else:
            visitados.append((x, y))
    return False

path = 'NESWW'

print(camino_recorrido(path))