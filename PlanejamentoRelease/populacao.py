from venv.PlanejamentoRelease.main import *
import random
import copy


class Populacao:

    def individuo(self, min, max):
        return [random.randint(min, max) for i in range(tam_individuo)]

    def criar_populacao(self):
        return list(self.individuo(1, 3) for i in range(tam_populacao))

    def custo(self):
        custo = (60, 40, 40, 30, 20, 20, 25, 70, 50, 20)  # valor informado na tabela
        return custo

    def calculo_custo(self, populacao):

        n = 0
        populacao = copy.deepcopy(populacao)
        populacao_viavel = list()
        solucao_invalida = 0

        custototal = list()
        orcamento = 125

        for i in populacao:
            custoR1, custoR2, custoR3 = 0, 0, 0
            n = 0

            while n < 10:

                if i[n] == 1:
                    custoR1 = Populacao().custo()[n] + custoR1

                    if custoR1 > orcamento:
                        solucao_invalida = 1
                        i[n] = 0
                        populacao_viavel = populacao
                        custoR1 = custoR1 - Populacao().custo()[n]

                if i[n] == 2:
                    custoR2 = Populacao().custo()[n] + custoR2

                    if custoR2 > orcamento:
                        solucao_invalida = 1
                        i[n] = 0
                        populacao_viavel = populacao
                        custoR2 = custoR2 - Populacao().custo()[n]

                if i[n] == 3:
                    custoR3 = Populacao().custo()[n] + custoR3

                    if custoR3 > orcamento:
                        solucao_invalida = 1
                        i[n] = 0
                        populacao_viavel = populacao
                        custoR3 = custoR3 - Populacao().custo()[n]

                n += 1
            custototal.append([custoR1, custoR2, custoR3])

        if solucao_invalida == 1:
            solucao = populacao_viavel
            print("\nPopulacao Viavel", populacao_viavel)
        else:
            solucao = populacao

        print("\nCusto Requisitos por individuo: ", custototal, "\n")

        return solucao
