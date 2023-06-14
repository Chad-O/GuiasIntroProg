import random

def main():
    listanombres = []
    listapesos = []
    res = 0
    cantidad = int(input("Cantidad de persona: "))
    for i in range(0,cantidad):
        nombre = input("Ingrese nombre: ")
        listanombres.append(nombre)

    for i in range(0, cantidad):
        listapesos.append(random.randint(29,50))
    print(listapesos)
    for i in range(0, cantidad):
        if listapesos[i] <= 35 and listapesos[i] >= 30:
            res = res + 1

    print("La cantidad de personas que pesan entre 30 y 35 son: ", res)
main()