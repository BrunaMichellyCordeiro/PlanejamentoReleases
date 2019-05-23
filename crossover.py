import random
import copy
custo = (60, 40, 40, 30, 20, 20, 25, 70, 50, 20)


class Crossover:

    def cruzamento(self, pais, taxacross):   ##recebe os pais que foram selecionados no torneio

        taxacrossover = random.randint(0, 100)
        corte = random.randint(1, 9)
        aux = copy.deepcopy(pais)  ###valor do torneio
        pai1 = aux[0]
        pai2 = aux[1]
        custoCros = list()

        if taxacrossover == taxacross:
            fatiaPai1 = pai1
            fatiaPai2 = pai2
            filho1 = (fatiaPai1[:corte] + fatiaPai2[corte:])
            filho2 = (fatiaPai2[:corte] + fatiaPai1[corte:])

            filhos = filho1, filho2

            for i in filhos:
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
                custoCros.append([custoR1, custoR2, custoR3])

            for i in custoCros:
                n = 0
                while n < 3:
                    if i[n] > 125:   #se o custo do crossover for maior do que o orcamento retorna os pais
                        filhos = pais
                        n = 10
                    n += 1
        else:
            filhos = pais

        return filhos
