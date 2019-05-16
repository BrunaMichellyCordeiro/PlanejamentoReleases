import copy
import random

custo = [60, 40, 40, 30, 20, 20, 25, 70, 50, 20]  # valor informado na tabela


class Mutacao:

    def mutacao(self, filhos, custototal):      #recebe os filhos do crossover

        aux = copy.deepcopy(filhos)         #copia dos filhos
        filho1 = aux[0]
        filho2 = aux[1]

        orcamento = 125
        custototal = copy.deepcopy(custototal)
        n = 0

        ind = list()
        mutfilho1 = 0

        for i in custototal:
            n = 0

            while n < 3:
                if i[n] > orcamento:   #posicao 0 == custoR1
                    if mutfilho1 == 0:
                        n = random.randint(0, 3)
                        filho1[n] = random.randint(0, 3)
                        mutfilho1 = 1
                        break
                    else:
                        n = random.randint(0, 3)
                        filho2[n] = random.randint(0, 3)
                        break
                n += 1

        custoMutacao = Mutacao().custoCrossoverMutacao([filho1, filho2])

        if custoMutacao != custototal:

            for i in custoMutacao:
                n = 0
                while n > 10:
                    if i[n] > orcamento:   #posicao 0 == custoR1
                        if mutfilho1 == 0:
                            n = random.randint(0, 3)
                            filho1[n] = random.randint(0, 3)
                            mutfilho1 = 1

                        else:
                            n = random.randint(0, 3)
                            filho2[n] = random.randint(0, 3)
                    n += 1
                    
        print("Custo Mutação: ", custoMutacao)
        return [filho1, filho2]

    def custoCrossoverMutacao(self, individuo):

        custototal = list()

        for i in individuo:  # calcular o custo dos filhos do crossover
            custoR1, custoR2, custoR3 = 0, 0, 0
            n = 0

            while n < 10:

                if i[n] == 1:
                    custoR1 = custo[n] + custoR1

                if i[n] == 2:
                    custoR2 = custo[n] + custoR2

                if i[n] == 3:
                    custoR3 = custo[n] + custoR3

                n += 1

            custototal.append([custoR1, custoR2, custoR3])

        return custototal


