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

precio = int(input("ingrese el precio del producto"))
if precio <= 0:
    print("Verifica lo ingresado, no puede ser negativo")
else:
    break

