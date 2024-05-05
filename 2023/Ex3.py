def es_primo(n,div = 0,it = 1):
    if div == 2 and n == it-1:
        return True
    elif div > 2:
        return False
    else:
        if n%it == 0:
            return es_primo(n,div+1,it+1)
        else:
            return es_primo(n,div,it+1)

def main():
    numbers = list(range(2, 101))
    for n in numbers:
        r = es_primo(n)
        if r:
            print(n," es primo")
        else:
            print(n," no es primo")
main()

