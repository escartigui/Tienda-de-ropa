tienda= []
cantidad = int(input(f"\nIngrese la cantidad de sus productos: "))
for i in range(cantidad):
    print(f"\nproductos #{i+1}")

    while True: #este servira como mi verificador
        codigo = input(f"\nIngrese el codigo del producto: ")
        if codigo in tienda:
            print("codigo ya utilizado")
        else:
            break

nombre = input("Nombre del Producto")
categoria = input("Categoria (hombre,mujer,niño)")
talla = input("Talla (XS,S,M,L,XL)")

while True:
 precio = int(input("ingrese el precio del producto"))
 if precio <= 0:
    print("Verifica lo ingresado, no puede ser negativo")
 else:
    break

while True:
    stock = int(input(f"\nIngrese la cantidad los producto: "))
    if stock <= 0:
        print("Verifica lo ingresado, no puede ser negativo")
    else:
        break

tienda[codigo] = {
    'nombre': nombre,
    'categoria': categoria,
    'talla': talla,
    'precio': precio,
    'stock': stock,
}
print("\nLista de estudiantes: ")
for codigo,datos in tienda.items():
    print(f"codigo: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Categoria: {datos['categoria']}")
    print(f"Talla: {datos['talla']}")
    print(f"Precio: {datos['precio']}")
    print(f"Stock: {datos['stock']}")

print("buscar")
encontrado = input(f"\nIngrese el codigo para poder encontrarlo: ")
if encontrado in tienda:

