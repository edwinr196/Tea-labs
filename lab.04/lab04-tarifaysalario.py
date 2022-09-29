def calcularpago(horas, tarifa): 
    MAX_HORAS = 40
    if (horas > MAX_HORAS):
        horas_extras = horas - MAX_HORAS
    calculo = (horas * tarifa) + (horas_extras * (tarifa / 2))
    return calculo

try:
    horas = float (input("ingrese numero de horas: "))
    tarifa = float (input("ingrese tarifa: "))
    pago = calcularpago(horas, tarifa)
    print(pago)
except:
    print("Error, valor ingresado no es válido")