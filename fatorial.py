def main():
    n = int(input("Digite o valor de n: "))
    fat = 1                 #fat = 1 pois o fatorial de 0 é 1
    i = 1                   # i = 1
    while i <= n:           #i= 1<=5
        fat = fat*i         #fat = 1*2 = 2   fat= 1*1 = 1
        i = i + 1

    print(fat)

main()
