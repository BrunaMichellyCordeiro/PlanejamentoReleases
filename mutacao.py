import copy
import random

custo = [60, 40, 40, 30, 20, 20, 25, 70, 50, 20]  # valor informado na tabela
orcamento = 125

class Mutacao:

    def mutacao(self, filhos, taxamut):      #recebe os filhos do crossover

        aux = copy.deepcopy(filhos)         #copia dos filhos
        filho1 = aux[0]
        filho2 = aux[1]
        taxamutacao = random.randint(0, 100)
        filho = list()
        customutacao = list()

        if taxamutacao == taxamut:
            m = random.randint(0, 9)
            filho1[m] = random.randint(0, 3)
            n = random.randint(0, 9)
            filho2[n] = random.randint(0, 3)
            filho = filho1, filho2

            for i in filho:
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
                customutacao.append([custoR1, custoR2, custoR3])

            for c in customutacao:
                n = 0
                while n < 3:
                    if c[n] > 125:
                        filho = filhos
                    n += 1

        else:
            filho = filhos

        return filho
