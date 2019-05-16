import numpy as np

def invmat(a):

    id = np.zeros((a, a))     #id matriz identidade com zeros
    i = 1

    for i in [1, a]:
        id(i, i) = 1
    end

    return id


dim = int(input("informe a dimensão da matriz nxn: "))
fun = invmat(dim)
print(fun)


