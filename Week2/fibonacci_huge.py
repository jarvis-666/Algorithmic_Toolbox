if __name__ == '__main__':
    def calc_fibo(n):
        F = list()
        F.append(0)
        F.append(1)
        for i in range(2, n + 1):
            F.append(F[i - 1] + F[i - 2])
        return F[n]

    def calc_fibo_huge(n, m):
        if n <= 1:
            return n
        prev = 0
        curr = 1
        for i in range(m*m + 1):
            prev, curr = curr, (prev + curr) % m
            if prev == 0 and curr == 1:
                remainder = n % (i + 1)
                return calc_fibo(remainder) % m

    n, m = map(int, input().split())
    print(calc_fibo_huge(n, m))