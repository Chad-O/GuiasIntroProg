def problema1():
    pies = float(input("Ingresar el valor: "))
    conv = 0.3048
    print("El valor en metros es: " + str(pies*conv))

def problema2():
    pesoLibras = float(input("Ingresar el valor en libras: "))
    L = 0.4536
    pesoK = pesoLibras*L
    print("El valor en kilogramos es: " + str(pesoK))

def problema3():
    radio = float(input("Ingresar el radio: "))
    longitud = float(input("Ingresar la longitud: "))
    
    pi = 3.1416
    area = radio*pi*radio
    volumen = area*longitud

    print("El área es:  " + str(area))
    print("El volumen es: " + str(volumen))
        
def problema4():
    subtotal = float(input("Ingresar el subtotal: "))
    tasa = float(input("Ingresar la tasa (ej. 0.2): "))
    gratuidad = tasa * subtotal
    total = subtotal + gratuidad
    print("La gratuidad es " + str(gratuidad))
    print("El total es " + str(total))
    
def problema5():
    VI = float(input("Ingresar velocidad inicial: "))
    VF = float(input("Ingresar velocidad final: "))
    t = float(input("Ingresar el tiempo: "))
    
    acc = (VF-VI) / t
    print("La aceleración promedio es " + str(acc) + " metros por segundo")

def problema1B():
    tasa = float(input("Ingresar la tasa: "))
    deposito = float(input("Ingresar el deposito mensual: "))
    res = 0
    TEM = ((1+tasa)**(1/12))-1
    
    #sin bucle
    res = (deposito+res) * (1+TEM) #mes 1
    res = (deposito+res) * (1+TEM) #mes 2
    res = (deposito+res) * (1+TEM) #mes 3
    res = (deposito+res) * (1+TEM) #mes 4
    
    print(res)

def problema2B():
    x = float(input("Ingresar valor de x: "))
    x = x**4 + x**3 + 2*x**2 - x
    print(x)
    
def problema3B():
    pesoLibras = float(input("Ingresar peso en libras: "))
    alturaPulgadas = float(input("Ingresar altura en pulgadas: "))
    L = 0.4536
    P = 0.0254
    pesoK = pesoLibras * L
    alturaM = alturaPulgadas * P
    
    IMC = pesoK / (alturaM**2)
    print("El índice de masa corporal es: " + str(IMC))
    
def problema4B():
    infIni = int(input("Ingresar cantidad de personas infectadas inicialmente: "))
    e = 2.72
    t = int(input("Ingresar dias desde el inicio de la infección: "))
    
    infTotal = infIni * e ** (5*t)
    # La cantidad de personas es un número entero
    infTotal = int(infTotal)
    print("La cantidad de personas infectadas en el día " + str(t) + " es: " + str(infTotal))

def problema5B():
    oper1 = float(input("Ingresar primer operando: "))
    oper2 = float(input("Ingresar segundo operando: "))
    operacion = input("Ingresar símbolo de operacion: ")
    res = 0
    
    if operacion == "+":
        res = oper1 + oper2
    elif operacion == "-":
        res = oper1 - oper2
    elif operacion == "*":
        res = oper1 * oper2
    elif operacion == "/":
        res = oper1 / oper2
    else:                               #un simbolo fuera de las opciones
        res = "Simbolo no reconocido"
    
    print("El resultado es: " + str(res))

def problema6B():
    #No hay necesidad de programa en python
    pass
    
def problema7B():
    radio = float(input("Ingresar el radio: "))
    pi = 3.1416
    area = pi * radio * radio
    perimetro = 2 * pi * radio
    print("El área de la circunferencia es: " + str(area))
    print("El perimetro de la circunferencia es: " + str(perimetro))

def problema8B():
    catA = float(input("Ingresar longitud de cateto A: "))
    catB = float(input("Ingresar longitud de cateto B: "))
    c = (catA**2 + catB**2)**0.5 # 0.5 == 1/2
    print("La hipotenusa del triangulo es: " + str(c))
    
def main():
    problema8B()
    print("Fin de la guía")
main()