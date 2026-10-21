def productos_en_oferta(inventario, precio_max):
    productos = []
    for producto in inventario:
        producto_precio = inventario[producto]
        if producto_precio['precio'] <= precio_max and producto_precio['oferta'] == True:
            productos.append(producto)
        else:
            continue
    return productos

tienda = {
    'Camisa': {'precio': 20, 'oferta': True},
    'Pantalón': {'precio': 35, 'oferta': False},
    'Zapatos': {'precio': 15, 'oferta': True},
    'Chaqueta': {'precio': 25, 'oferta': True}
}
presupuesto = int(input('Ingrese su presupuesto: '))

print('Puede comprar:', productos_en_oferta(tienda, presupuesto))

# Salida esperada para productos_en_oferta(tienda, 20):
# ['Camisa', 'Zapatos']