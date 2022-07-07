# This is a sample Python script.

import array as arr

def KS(M, w, v, n, C):
    if M[n][C] != 0: return M[n][C]
    if n == 0 or C==0 :
        result = 0
    else :
        if w[n] > C :
            result = KS(M, w, v, n-1, C)
        else:
            tmp1 = KS(M, w, v, n-1, C)
            tmp2 = v[n] + KS(M, w, v, n-1, C-v[n])
            result = max(tmp1, tmp2)
            M[n][C] = result
    return M

if __name__ == '__main__':
    W = 8
    n = 5
    w = [0, 2, 1, 3, 2, 4, 0]
    v = [0, 3, 4, 7, 6, 9, 0]
    # M =[[0 for j in range(W)] for i in range(n)]
    M = [[0]*(W+1) for i in range(n+1)]

    print('stage1: ',M)
    x = KS(M, w, v, n, W)
    print('stage2: ',M)
