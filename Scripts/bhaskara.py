import math


def delta(a, b, c):
    return b ** 2 - 4 * a * c


def bhaskara(a, b, c):

    if delta(a, b, c) == 0:
        raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        print("unica raíz: ", raiz1)
    if delta(a, b, c) < 0:
        print("nao possui valores reais")
    else:
        raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        raiz2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
        print("Raiz 1: ", raiz1)
        print("Raiz 2: ", raiz2)


def main():

    a = int(input("Informe o valor de a: "))
    b = int(input("Informe o valor de b: "))
    c = int(input("Informe o valor de c: "))
    bhaskara(a, b, c)


main()

