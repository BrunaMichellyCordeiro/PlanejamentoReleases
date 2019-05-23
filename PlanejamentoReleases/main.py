from venv.PlanejamentoRelease.populacao import *
from venv.PlanejamentoRelease.modelagem import *
from venv.PlanejamentoRelease.selecao import *
from venv.PlanejamentoRelease.crossover import *
from venv.PlanejamentoRelease.mutacao import *

tam_individuo = 10  # definição da quantidade de individuos em cada solução
tam_populacao = 10  # definição da população total
orcamento = 125
taxamut = random.randint(0, 5)     #taxa de até 5% de mutaçao
taxacross = random.randint(0, 100)   #taxa de 60% de cruzamento


def main():

    n = 0
    custo = [60, 40, 40, 30, 20, 20, 25, 70, 50, 20]
    custoR1, custoR2, custoR3 = 0, 0, 0
    populacaofinal = list()
    ind = list()
    fitfinal = list()
    individuo = list()
    individuo2 = list()
    solucao = list()
    melhor = list()
    custofinal = list()

    print("\n------------------------Informações do problema ------------------------")
    print("Importancia:", Modelagem().importancia())
    print("Risco: \t\t", Modelagem().risco())
    print("Custo: \t\t", custo)
    print("Orçamento:    R$ 125,00")
    print("\nTamanho da população:", tam_populacao)
    print("Quantidade de individuos: ", tam_individuo)
    print("-------------------------------------------------------------------------")

    #salvar na população final as alterações a populacao final tem que ser igual a população inicial

    tam_pop_final = 0

    while tam_pop_final < tam_populacao:

        populacaoCusto = Populacao().calculo_custo_reparar(Populacao().criar_populacao())
        populacao = populacaoCusto[0]
        fitness = FuncaoFitness().funcaoFitness(populacao)
        pais = Selecao().torneio(fitness, populacao)
        cruzamento = Crossover().cruzamento(pais, taxacross)
        mutacao = Mutacao().mutacao(cruzamento, taxamut)
        fitfinal = FuncaoFitness().funcaoFitness(mutacao)
        populacaofinal.append([mutacao, fitfinal])
        tam_pop_final += 1

    for ind in populacaofinal:
        individuo = ind[0]
        fit = ind[1]

        ind1 = individuo[0]
        fit1 = fit[0]
        ind2 = individuo[1]
        fit2 = fit[1]

        individuo1 = ind1, fit1
        individuo2 = ind2, fit2
        maximo = max(fit1, fit2)
        melhor.append(maximo)

        #print("Maximo", maximo)
        #print("\nIndividuo1: ", individuo1)
        #print("Individuo2:", individuo2, "\n")

        solucao.append([individuo1, individuo2])

    solucaofinal = max(melhor)

    for s1 in solucao:
        for s2 in s1:
            if s2[1] == solucaofinal:
                indfinal = s2[0]

    while n < 10:

        if indfinal[n] == 1:
            custoR1 = custo[n] + custoR1

        if indfinal[n] == 2:
            custoR2 = custo[n] + custoR2

        if indfinal[n] == 3:
            custoR3 = custo[n] + custoR3
        n += 1

    custofinal.append([custoR1, custoR2, custoR3])

    print("\n\nSolução final: \nIndividuo: ", indfinal, "\nFitness: ", solucaofinal)
    print("Custo:", custofinal)


if __name__ == '__main__':
    main()
