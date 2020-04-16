# program to calculate the nth fibonacci number
if __name__ != '__main__':
    def calc_fibo(n):
        if n <= 1:
            return n
        else:
            return calc_fibo(n-1) + calc_fibo(n-2)

    n = int(input())
    print(calc_fibo(n))

if __name__ == '__main__':
    def calc_fibo(n):
        F = []
        F.append(0)
        F.append(1)
        for i in range(2, n + 1):
            F.append(F[i - 1] + F[i - 2])
        return F[n]

    n = int(input())
    print(calc_fibo(n))
