def maxAdRev(n, a, b):
    dot_prods = [a[i] * b[i] for i in range(n)]
    rev = sum(dot_prods)
    return rev

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))         # profit per click of ith ad
    b = list(map(int, input().split()))         # average number of clicks per day of ith slot
    a.sort(reverse = True)
    b.sort(reverse = True)
    print(maxAdRev(n, a, b))