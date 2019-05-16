def fatorial (n):           #calcular o fatorial de n
    fat = 1                 #fat = 1 pois o fatorial de 0 é 1
    i = 1                   # i = 1
    while i <= n:           #i= 1<=5
        fat = fat*i         #fat = 1*2 = 2   fat= 1*1 = 1
        i = i + 1

    return fat


def main():

    print("Calculo dos coeficientes binomiais")
    fatN = int(input("Valor de n: "))
    fatP = int(input("Valor de p: "))

    numN = fatorial(fatN)
    numP = fatorial(fatP)
    difNP = (fatN - fatP)

    binomial = int((numN/(numP*fatorial(difNP))))

    print(binomial)


main()

