def calc_fibo_sum(n):
    prev = 0
    curr = 1
    sum = 1
    for i in range(2, n + 1):
        prev, curr = curr % 10, (prev + curr) % 10
        sum = sum % 10 + curr % 10
    return sum % 10

def calc_fibo_sum_last_digit(n):
    if n <= 1:
        return n
    divisions = n / 60
    sum_of_first_60 = calc_fibo_sum(59)
    remainder = n % 60
    sum_of_remainder = calc_fibo_sum(remainder)
    if n % 60 == 0:
        return int((sum_of_remainder + divisions * sum_of_first_60) % 10) - 1
    return int((sum_of_remainder + divisions * sum_of_first_60) % 10)

n = int(input())
print(calc_fibo_sum_last_digit(n))