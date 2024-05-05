import random

def promedio(lista):
    acumulador = 0
    cantidad = 0
    for i in range(0,len(lista)):
        acumulador = acumulador + lista[i]
        cantidad = cantidad + 1
    return acumulador/len(lista)

def es_primo(lista):
    listaprimos = []
    for i in range(0,len(lista)):
        cont = 0
        for j in range(1,lista[i]+1):
            if lista[i]%j == 0:
                cont += 1
        if cont == 2:
            listaprimos.append(lista[i])
    return listaprimos

def multiplos2y6(lista):
    acum = 0
    listares = []
    for n in range (0, len(lista)):
        val = lista[n]
        if val%2 == 0 and val%6 == 0:
            listares.append(val)
    return listares
        

def problema2(base, exp):
    if exp == 1:
        return exp/pow(base,exp)
    else:
        return exp/pow(base,exp) + problema2(base,exp-1)  
    
def main():
    print(problema2(5,2))

    #lista = []
    #for i in range(0,180):
     #   lista.append(random.randint(140,850))
    
    #print("El promedio de la lista es: ", promedio(lista))
    #print("Hay: ", es_primo(lista), " numeros primos en la lista")
    #print("Los numeros que son multiplos de 2 y 6 son: ", multiplos2y6(lista))
main()