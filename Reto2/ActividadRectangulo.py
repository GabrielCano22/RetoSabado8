#Se piden los datos del rectangulo por teclado

print("###Programa del rectángulo###")
ancho = int(input("Por favor ingrese el ancho del rectángulo: "))
alto = int(input("Por favor ingrese el alto del rectángulo: "))
area = int(ancho * alto)
print(f'El area del rectangulo es: {area}') 


ladoSuperioreInferior = int(ancho * 2)
ladoIzquierdayDerecha = int(alto * 2)

perimetro = ladoSuperioreInferior + ladoIzquierdayDerecha
print(f'El perimetro del rectangulo es: {perimetro}')

for i in range(alto):
    for j in range(1, ancho + 1):
        print("*",end="")
    print(" ")

# for i in range(1, alto + 1):
#     for j in range(1, ancho + 1):
#         print("*",end="")
#     print(" ")
