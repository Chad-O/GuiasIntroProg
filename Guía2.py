import math

def problema1():
    gasto = int(input("Ingrese la cantidad de pago: "))
    if(gasto <= 100):
        print("Paga en efectivo")
    elif(gasto < 300):
        print("Paga con tarjeta de debito")
    else:
        print("Paga con tarjeta de credito")
    
def problema2():
    x = int(input("Ingrese el numero 1: "))
    y = int(input("Ingrese el numero 2: "))
    print(x//y)

def problema3():
    x = int(input("Ingrese el numero 1: "))
    y = int(input("Ingrese el numero 2: "))
    if(x > y):
        print(x, " Es mayor que ", y)
    elif(x < y):
        print(y, " Es mayor que ", x)
    else:
        print("Son iguales")

def problema4():
    añoActual = int(input("Ingrese el año actual: "))
    añoCualq = int(input("Ingrese el año a comparar: "))
    if(añoActual > añoCualq):
        print("El año ", añoCualq, " paso hace ", añoActual - añoCualq, " años")
    elif(añoCualq > añoActual):
        print("Faltan ", añoCualq - añoActual, " años para el año", añoCualq)
    else:
        print("Son el mismo año")

def problema5():
    x = int(input("Ingrese el numero 1: "))
    y = int(input("Ingrese el numero 2: "))
    z = int(input("Ingrese el numero 3: "))
    if(x == y and y == z):
        print("Los 3 numeros son iguales")
    elif((x == y or x == z or y == z) and (x != z or x != y or y != z)):
        print("Solo 2 numeros son iguales")
    else:
        print("Todos son distintos")

def problema6():
    a = int(input("Ingrese el valor del numero a: "))
    b = int(input("Ingrese el valor del numero b: "))
    c = int(input("Ingrese el valor del numero c: "))

    discrimante = b**2 - 4*a*c
    
    if(discrimante > 0):
        rdisc = math.sqrt(discrimante)
        r1 = float(-b + rdisc)/(2*a)
        r2 = float(-b - rdisc)/(2*a)
        print("Raiz 1: ", r1)
        print("Raiz 2: ", r2)
    elif(discrimante == 0):
        rdisc = math.sqrt(discrimante)
        r1 = float(-b + math.sqrt(discrimante))/(2*a)
        print("Raiz 1: ", r1)
    else:
        print("La ecuacion no tiene raices reales")

def problema7():
    x = int(input("Ingrese monto: "))    
    
    if(x > 5000):
        inter = 0.08
        pago = x*inter + x
    elif(x == 5000):
        inter = 0.05
        pago = x*inter + x
    elif(x >= 1000):
        inter = 0.04
        pago = x*inter + x

    print("Se pagara el monto: ", pago)

def problema8():
    x = int(input("Ingrese el año: "))

    if(x%4==0  and( x%100!=0 or x%400==0)):
        print("Es año bisiesto")
    else:
        print("No es año bisiesto")
    
def problema9():
    pagoxHora= int(input("Ingrese el pago por hora: "))
    horasCumplidas = int(input("Ingrese las horas trabajadas: "))

    if(horasCumplidas > 60):
        pago = pagoxHora * horasCumplidas *3 + 2000
    elif(horasCumplidas <= 60 and horasCumplidas >= 51):
        pago = pagoxHora * horasCumplidas*3
    elif(horasCumplidas <= 50 and horasCumplidas >= 41):
        pago = pagoxHora * horasCumplidas*2
    else:
        pago = pagoxHora *horasCumplidas
    
    print("El pago total es: ", pago)

def problema10():
    cobro = 2.5
    horas = int(input("Ingrese la cantidad de horas: "))
    minutos = int(input("Ingrese los minutos transcurridos: "))

    if(horas <= 1 and minutos == 0):
        print("No tiene que pagar estacionamiento")
    elif(horas > 1 and minutos > 0):
        print("Se debe pagar ", horas*cobro + cobro )
    elif(horas > 1 and minutos == 0):
        print("Se debe pagar ", horas*cobro )
        
def problema11():
    cantidad = int(input("Ingrese la cantidad de producto comprado "))
    monto = 2
    if(cantidad < 36):
        desc = 0.1
        pago = monto * cantidad *desc + monto * cantidad
    else:
        desc = 0.15
        pago = monto * cantidad *desc + monto * cantidad
        cantidad = cantidad + ((cantidad - 36)//12)
    
    print("Cantidada a pagar: ", pago)
    print("Unidades extra: ", ((cantidad - 36)//12))
    print("Cantidad total: ", cantidad)
        

def main():
    problema11()
    print("Fin de la guía")
main()