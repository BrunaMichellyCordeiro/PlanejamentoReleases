def main():
    n = int(input("Digite um número inteiro: "))

    i = 0
    while n > 0:   #n = 122, i = 0
            ultimoD = n%10    # ultimoD = 2
            n = n//10           # n = 12 dessa forma é possível atualizar sempre o valor de n
            testIgual = n%10   # testIgual = 2
            if(testIgual >= 0) and (ultimoD == testIgual):
                i = i+1
    if i > 0:
        print("sim")
    else:
        print("nao")
main()