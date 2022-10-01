print('PROGRAMA AREGLO DE 20 NUMEROS')
numeros = []


def perdirNumeros(numeros):
    while len(numeros) < 5:
        try:
            r = int(input('Ingrese el numero: '))
            if r >= 0:
                numeros.append(r)
            else:
                print(
                    f'{r} no es un valor valido,debe digitar un numero igual o mayor que cero')
        except ValueError:
            print('ValorInvalido: ha digitado una letra')
    return numeros


perdirNumeros(numeros)


def sumarDatosArray(numeros):
    suma = 0
    for i in numeros:
        suma += i
    return suma, len(numeros)


datos = list(sumarDatosArray(numeros))
print(datos)

# Calculated as the average of the sum of


def dividir(numeros):
    promedio = numeros[0] / numeros[1]

    return promedio


print(f'El promedio de la suma es de: {dividir(numeros)}')
