def encontrar_cumbres(alturas, k):
    vecinos = k // 2
    cumbres = []
    for i in range(vecinos, (len(alturas) - vecinos)):
        if alturas[i] > max(alturas[(i - vecinos) : i]) and alturas[i] > max(alturas[(i + 1) : (i + 1 + vecinos)]) :
            cumbres.append(alturas[i])
    return cumbres

L = [41, 10, 40, 70, 8, 50, 51, 2, 10, 90, 12]
k = 4

print(encontrar_cumbres(L,4))