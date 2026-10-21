def encontrar_valles(t):
    valles = []
    for i in range(1, len(t)):
        while (i + 1) < len(t):
            if t[i] < t[i - 1] and t[i] < t[i + 1]:
                valles.append(t[i])
            break
    return valles

temperaturas = [22, 18, 20, 25, 19, 23, 23, 21]

print('valles =', encontrar_valles(temperaturas))