def main():
    n = int(input("Digite um número inteiro:"))

    Soma = 0

    while(n > 0 ):
        ultimoD = n%10   #3,2,1
        n = n//10    #12,1,0
        Soma = ultimoD+Soma #3+0=3,2+3=5,1+5=6

    print(Soma)
main()