lista = [1, 2, 'kkk', 'jjj']

for i in lista:
    print(lista)

for i in range(10,20,2):
    print(i)

a = "Bruna"
b = "Michelly"

concat = a + " " + b

print(concat)
print(concat[0:7])

print(concat.lower())   #tudo minúsculo
print(concat.upper())   #tudo maiúsculo

minha_string = "O rato roeu a roupa do rei de Roma"

#minha_lista = minha_string.split("r")           #transformar uma string em um vetor/lista, também é utilizado para quebrar uma string sempre que ver uma letra específica
minha_lista = minha_string.split(" ")
print(minha_lista)

busca = minha_string.find("rei")            #imprime a posição na lista onde começa a palavra - caso não encontre o valor buscando o retorno é -1
print(busca)

print(minha_string[busca:])     #Imprime da posição de busca até a última  posição

minha_string = minha_string.replace("rei", "rainha")            #substituir uma determinada palavra por outra
print(minha_string)

