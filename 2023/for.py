list = [1,2,3,4,5,6,7,8]

#Equivalente a while normal:
for i in range(0,len(list)):
    print(list[i])

#While "normal":
i = 0
while i < len(list):
    print(list[i])
    i+=1
#Fin While "normal":

#For como iterador
for i in list:
    print(i)
