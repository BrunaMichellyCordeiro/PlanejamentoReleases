import numpy as np
import time


def gaussElimin(a, b):

    n = len(b)

# Fase de Eliminacao Progressiva
    for k in range(0, n-1):
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k]/a[k, k]
                a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
                b[i] = b[i] - lam*b[k]

# Fase de Substituicao Regressiva
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]

    return b


n = 2000
a = np.floor(10*np.random.random((n, n)))       #gerar uma matriz randomica nxn de valores até 10
b = np.arange(0,n,1)                            #gerar o vetor b de forma randomica variando de 0 a n de 1 em 1
x = gaussElimin(a, b)                           #chamando a função
print("Soluções: ",x)                           #impressão do resultado das soluções


inicio = time.time()                            #função time para início da execução da função
gaussElimin(a, b)                               #função a ser verificada
fim = time.time()                               #função time para fim da execução da função
print("tempo de execução: ", fim - inicio)      #Impressão do tempo de execução em segundos

