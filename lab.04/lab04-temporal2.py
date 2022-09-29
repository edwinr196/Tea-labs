contador = 0
sumatoria = 0
while True:
    input_str = input("ingrese un número: ")
    try:
        if (input_str == "done"):
            break
        else:
            contador = contador + 1
            sumatoria = sumatoria + int(input_str)
            promedio = sumatoria / contador
    except:
        print("Error, debe ingrsar un número")
        continue
print("Contador: ", contador)
print("Sumatoria: ", sumatoria)
print("Promedio: ", promedio)
