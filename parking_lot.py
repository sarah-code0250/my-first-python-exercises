 
print("Playa de estacionamiento")


horas = int(input("Ingrese las horas que se estaciono: "))


if horas == 1:
    pago = 1500
    print("Debe pagar: $", pago)


elif horas > 1:
    pago = 1500 + (horas - 1) * 1000
    print("Debe pagar: $", pago)


else:
    print("No debe pagar")
