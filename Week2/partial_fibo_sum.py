def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10
    return current

def partial_fibo_sum(f, t):
    f = f % 60
    t = t % 60
    if f == t:
        return get_fibonacci_last_digit(f)
    if f > t:
        t = 60 + t
    sum = 0
    for i in range(f, t + 1):
        fibo_last_digit = get_fibonacci_last_digit(i)
        sum = sum + fibo_last_digit
    return sum % 10

f, t = map(int, input().split())
print(partial_fibo_sum(f, t))