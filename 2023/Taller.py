import math

def problema1(n):
    if n == 0:
        return n
    else:
        return n + problema1(n-1)

def problema2(base, exp):
    if exp == 1:
        return base
    else:
        return base * problema2(base,exp-1)

def problema6(n):
    if n==0:
        return 0
    else:
        return n%10+problema6(n//10)

def problema8(n):
    if n == 1:
        return 1/2
    else:
        return (1/math.pow(2,n))+ problema8(n-1)
        

def problema11(x,lis,it,sum):
    if it == len(lis):
        return sum
    else:
        if lis[it] > x:
            return problema11(x,lis,it+1,sum+1)
        else:
            return problema11(x,lis,it+1,sum)

def problema13(n,cant):
    if cant == 0 or n <= 0:
        return n
    else:
        return n + problema13(n-2,cant-1)

def main():
    
    n = int(input("Ingrese un numero "))
    cantidad = 0
    if n%2 == 0:
        cantidad = 10
    else:
        cantidad = 5
    
    print(problema13(n,cantidad))

    """
    Problema11
    n = int(input("Ingrese un numero "))
    list = [1,2,3,4,5,6,7,8,9,10]
    it = 0
    sum = 0
    
    while it < len(list):
        if n < list[it]:
            sum +=1 
        it +=1

    print("Cantidad de numeros mayores a ", n, " son ", sum)
    print(problema11(n,list,it,sum))
    """

main()