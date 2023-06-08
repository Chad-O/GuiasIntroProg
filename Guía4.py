import random

def problema1():
    lista = [1,2,3,4,5,6]
    
    lista1 = [1,2,3,4,5,6]
    
    lista1[0] = lista[0]
    i = 1
    while(i < len(lista)):

        lista1[i] = lista[i]+lista1[i-1]
        i+=1
    
    print(lista)
    print(lista1)

def problema2():
    n = 0 
    lista = []
    i = int(input("Ingrese la cantidad de alumnos: "))
    while (n < i): 
        print("Ingrese la nota del alumno ", n+1, " : ")
        val = int(input())
        lista.append(val)
        n+=1
    lista.sort()

    i = len(lista)-1
    n = 1
    while(i >= 0):
        if(i >= len(lista)-3):
            if(i==len(lista)-1):
                print("A:")
            print( "Nota ", n,": ", lista[i])
            
        elif(i >= len(lista)-5):
            if(i==len(lista)-4):
                print("B:")
            print( "Nota ", n,": ", lista[i])
            
        elif(i >= len(lista)-7):
            if(i==len(lista)-6):
                print("C:")
            print( "Nota ", n,": ", lista[i])
        
        elif(i >= len(lista)-9):
            if(i==len(lista)-8):
                print("D:")
            print( "Nota ", n,": ", lista[i])

        else:
            print("E")
            print( "Nota ", n,": ", lista[i])
        
        n+=1
        i-=1
    
def problema3():

    i = 0
    lista = []
    # llenamos la lista
    while i < 10:
        x = int(input("Ingrese un número: "))
        lista.append(x)
        i = i + 1
    # mostrar elementos empezando desde el final
    i = 9
    while i >= 0:
        print(lista[i])
        i = i - 1
        
def problema4():
    i = 0
    numeros = []
    sum_total = 0
    while i < 100:
        val = random.randint(0,100)
        numeros.append(val)
        sum_total = sum_total + val
        i+=1
    promedio = sum_total/100
    print(numeros)

    contEncima = 0
    contDebajo = 0
    
    i=0
    while i < len(numeros):
        if(numeros[i] < promedio):
            contDebajo+=1
        else:
            contEncima +=1
        i+=1

    print("Existen ", contDebajo, " numeros debajo del promedio")
    print("Existen ", contEncima, " numeros encima del promedio")
            

def problema5():
    i = 0
    lista = []
    tmplist = []

    while i < 200:
        val = random.randint(0,20)
        lista.append(val)
        i+=1
    
    i = 0
    j = 1
    while i < len(lista):
        while j < len(lista):
            if(lista[i] == lista[j]):
               print(j)
               tmplist.append(j) 
            j+=1
        i+=1
    print(tmplist)
    i = len(tmplist)-1
    print(lista)

    if(i >= 0):
        while i >= 0:
            lista.pop(tmplist[i])
            print( "pop, ", tmplist[i] ) 
            i-=1

    print(lista)

def main():
    problema5()
    print("Fin de la guía")
main()