def maximo(n, m):

    if(n > m):
        print(n)
    else:
        print(m)


def main():

    print("Informe dois números inteiros")
    numN = int(input("Primeiro: "))
    numM = int(input("Segundo: "))

    maximo(numN, numM)


main()
