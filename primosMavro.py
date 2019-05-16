n = int(input("Digite:"))
count = 0
i = 1

while(i <= n):
    resto = n%i
    i = i + 1
    if(resto == 0):
        count = count + 1

if(count == 2):
    print("primo")
else:
    print("nao primo")