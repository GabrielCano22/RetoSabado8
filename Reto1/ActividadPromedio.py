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

    suma=0
    for i in numeros:        
        suma+=i       
    return suma,len(numeros)
datos=list(sumarDatosArray(numeros))
def promediar(datos):
    prom=float(datos[0]/datos[1])
    print(f'la suma de los datos ingreados es: {datos[0]} y el promedio es: {prom}')
promediar(datos)
print(datos)