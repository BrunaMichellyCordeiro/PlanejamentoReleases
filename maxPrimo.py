def maior_primo(n):

    val = 0
    for n in range(1, n+1):   #percorrer até o final - a função range exclui o ultimo valor, por isso tem que somar 1
        cont = 0
        for i in range(1, n+1):   #verificar se é primo
            if n % i == 0:          # n é divisível por i
                cont += 1
        if cont <= 2:
            val = n
    print(val)


def main():

    num = int(input("Informe um número: "))

    if num >= 2:
        maior_primo(num)
    else:
        print("O número informado precisa ser maior ou igual a 2")

main()
