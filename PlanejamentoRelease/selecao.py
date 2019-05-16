import random
import copy


class Selecao:

    def torneio(self, fitness, individuo):

        k = 2
        n = 0
        pai1 = list()
        pai2 = list()

        escolha = copy.deepcopy(fitness)
        torneio = random.sample(escolha, k)

        fitpai1 = torneio[0]
        fitpai2 = torneio[1]

        for i in fitness:
            if fitpai1 == fitness[n]:
                #print("Pai 1: ", fitpai1, individuo[n])
                pai1 = [fitpai1, individuo[n]]
            if fitpai2 == fitness[n]:
                #print("Pai 2: ", fitpai2, individuo[n])
                pai2 = [fitpai2, individuo[n]]
            n += 1

        return [pai1, pai2]



