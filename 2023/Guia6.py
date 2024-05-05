def problema1(n, m, sum):
    if m == n+1:
        print(sum)
        return 0
    else:
        return problema1(n,m+1,sum+m)

def problema11(lis, n, it, sum):
    if it == len(lis):
        return sum
    else:
        if lis[it] > n:
            return problema11(lis,n,it+1,sum+1)
        else:
            return problema11(lis,n,it+1,sum)

def problema12(x, sum):
    if x == 0:
        return sum + 4
    else:
        return problema12(x-1,sum+16)


def problema13(n,cant):
    if cant == 0 or n == 0:
        return 0
    else: 
        print(n)
        return n + problema13(n-2,cant-1)

def main():
    """
    Problema 11
    lis = [1,2,3,4,5,6,7,8]
    n = 3
    it = 0
    sum = 0
    print(problema11(lis,n,it,sum))
    """
    """
    Problema12
    sum = 0
    n = int(input("Numero: "))
    print(problema12(n,sum))
    """
    """
    Problema13
    n = int(input("ingresa num: "))
    cantPares = 10
    cantImpares = 5
    if n%2 == 0:
        print("Suma Pares: ", problema13(n,cantPares))
    else:
        print("Suma Impares: ", problema13(n,cantImpares))
    """
    """
    Problema1
    n = int(input())
    m = 0
    sum = 0
    problema1(n, m, sum)
    """
main()