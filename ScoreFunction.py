def score(p, w, risco, S, V):

    importancia = [0]*10
    score = 0

    for i in range(10):

        for j in range(3):
            importancia[i] += w[j] * V[i][j]

        if S[i] != 0:
            score += importancia[i] * (p - S[i] + 1) - (risco[i] * S[i])

    return score

def main():

    p = 3
    w = [3, 4, 2]
    risco = [3, 6, 2, 6, 4, 8, 9, 7, 6, 6]
    S = [2, 0, 1, 1, 3, 0, 3, 1, 2, 1]
    V = [[10, 10, 5],
         [8, 10, 6],
         [6, 4, 8],
         [5, 9, 1],
         [7, 7, 5],
         [8, 6, 2],
         [6, 6, 4],
         [9, 8, 3],
         [6, 7, 5],
         [10, 10, 7]]

    print("Score:", score(p, w, risco, S, V))


if __name__ == "__main__":
    main()