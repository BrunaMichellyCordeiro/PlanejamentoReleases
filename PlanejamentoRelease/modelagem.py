import numpy as np


class Modelagem:
    def __init__(self):
        pass

    def importancia(self):  # calcular a importancia - trasformar a parte de tres colunas da tabela em uma coluna

        cliente_requisito = np.array(
            [[10, 10, 5], [8, 10, 6], [6, 4, 8], [5, 9, 1], [7, 7, 5], [8, 6, 2], [6, 6, 4], [9, 8, 3], [6, 7, 5],
             [10, 10, 7]])  # criação da matriz contendo os clientes e os requisitos V(ci,rj)
        relevancia = np.array([3, 4, 2])  # array de relevancia dos clientes
        produto = relevancia * cliente_requisito
        res_importancia = list(produto.sum(axis=1))  # soma das linhas de produto para retornar um unico vetor

        return res_importancia

    def risco(self):
        risco = (3, 6, 2, 6, 4, 8, 9, 7, 6, 6)  # valor informado na tabela
        return risco


class FuncaoFitness:

    def funcaoFitness(self, populacao):

        n = 0
        imp = Modelagem().importancia()
        ris = Modelagem().risco()
        y = np.ones(10, int)
        res_fitness = []
        #xi = np.array([1, 2, 3, 2, 1, 1, 0, 3, 2, 1])

        for ind in populacao:

            while n < 10:
                if ind[n] == 0:
                    y[n] = 0
                n += 1

            ind = np.array(ind)
            val = (3 - ind + 1)
            fitness = (imp * val - ris * ind) * y
            res_fitness.append(fitness.sum(axis=0))

        return res_fitness

