nombresProductos = [item.strip() for item in input("\nIngrese los productso separados por comas: \n").split(",")]
preciosProductos = [float(item.strip()) for item in input("\nIngrese los  percios separados por comas en el mismo orden que los nombres de los productos: \n").split(",")]

total = sum(preciosProductos)
descuento = 0

if total < 50000:
    print(f"\nse recomienda pagar en efectivo y obtendra un descuento del 5%\n")
    descuento = total * 0.05
elif total > 50000 and total <= 100000:
    print(f"\nse recomienda pagar con targeta tener en cuenta que no tendrea cambio, haz el pago preciso!! \n") 
else:
    print(f"\nse recibe pasgo por transferencia y se le dara un cashback del 2%\n")
    
print(f"\n\nproducto\tPrecio\n")

for nombre, precio in zip(nombresProductos, preciosProductos):
    print(f"{nombre}\t\t${precio:.2f}")

print(f"\n\nEl total a pagar es: ${(total - descuento):.2f}")