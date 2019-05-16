from venv.PlanejamentoRelease.populacao import *
from venv.PlanejamentoRelease.modelagem import *
from venv.PlanejamentoRelease.selecao import *
from venv.PlanejamentoRelease.crossover import *
from venv.PlanejamentoRelease.mutacao import *

tam_individuo = 10  # definição da quantidade de individuos em cada solução
tam_populacao = 4  # definição da população total


def main():

    print("Importancia:", Modelagem().importancia())
    print("Risco: ", Modelagem().risco())

    populacao = Populacao().calculo_custo(Populacao().criar_populacao())
    fitness = FuncaoFitness().funcaoFitness(populacao)
    pais = Selecao().torneio(fitness, populacao)
    cruzamento = Crossover().cruzamento(pais)
    custo_filhos = Mutacao().custoCrossoverMutacao(cruzamento)

    print("Fitness da populacao", FuncaoFitness().funcaoFitness(populacao))
    print("\nSeleção - Torneio: ", pais, "\n")
    print("\nFilhos - Crossover: ", cruzamento)
    print("Custo Filhos Crossover: ", custo_filhos, "\n")
    mutacao = Mutacao().mutacao(cruzamento, custo_filhos)
    print("Mutacao: ", mutacao)


if __name__ == '__main__':
    main()
