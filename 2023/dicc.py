from datos import datos as d

def almacenar():
    listah = []
    listam = []
    for i in d:
        if i["gender"] == "female":
            listam.append(i["age"])
        else:
            listah.append(i["age"])
    i = 0
    cont = 0
    while i < len(listah):
        j = 0
        while j < len(listam):
            if listah[i] > listam[j]:
                cont += 1
                j = len(listam)
            j += 1
        i += 1
    #print(listah)
    #print(listam)
    #print(cont)
    return listam,listah

def recdicc(val,lm,it):
    if val > lm[it]:
        return 1
    elif it == len(lm)-1:
        return 0
    else:
        return recdicc(val,lm,it+1)

def main():
    tupl = almacenar()
    i = 0 
    cont = 0 
    while i < len(tupl[1]):
        cont += recdicc(tupl[1][i],tupl[0],0)
        i += 1
    print(cont)

main()