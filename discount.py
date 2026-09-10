print("Descuento de producto")
precio = float(input("Ingrese el precio del producto: "))
docenas = int(input("Ingrese la cantidad de docenas: "))


costo_total = precio * docenas


if docenas > 3:
    descuento = costo_total * 0.15
else:
    descuento = costo_total * 0.10


costo_con_descuento = costo_total - descuento


print("Costo de la compra:", costo_total)
print("Descuento:", descuento)
print("Costo con descuento:", costo_con_descuento)
