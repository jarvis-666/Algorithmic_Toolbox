def knapsack(W, n, v, w, ratio_vw):
    A = [0] * n     # amounts that will be taken of each item
    V = 0           # the total of the fractional values
    for i in range(n):
        if W == 0:
            return V
        if w[i] > 0:
            a = min(W, w[i])
            A[i] = A[i] + a
            V = V + a * ratio_vw[i]
            w[i] = w[i] - a
            W = W - a
    return V


if __name__ == '__main__':
    n, W = map(int, input().split())
    v = []
    w = []

    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        w.append(b)

    ratio_vw = [v[i] / w[i] for i in range(n)]

    v = [a for _, a in sorted(zip(ratio_vw, v), reverse=True)]
    w = [b for _, b in sorted(zip(ratio_vw, w), reverse=True)]
    ratio_vw.sort(reverse=True)
    # print(ratio_vw)
    # print(v)
    # print(w)

    print("%.4f"%knapsack(W, n, v, w, ratio_vw))
