import random
import copy


class Crossover:

    def cruzamento(self, pais):   ##recebe os pais que foram selecionados no torneio

        corte = random.randint(1, 9)

        aux = copy.deepcopy(pais)     ###valor do torneio
        pai1 = aux[0]
        pai2 = aux[1]

        #print("fitness pai 1: ", pai1[0], "\nPai 1:", pai1[1], "\n\nfitness pai 2: ", pai2[0], "\nPai 2:", pai2[1])

        fatiaPai1 = pai1[1]
        fatiaPai2 = pai2[1]
        filho1 = (fatiaPai1[:corte] + fatiaPai2[corte:])
        filho2 = (fatiaPai2[:corte] + fatiaPai1[corte:])

        #print(filho1, filho2)

        return [filho1, filho2]



