def last_digit_sum_square(n):
    if n <= 1:
        return n
    n %= 60
    prev = 0
    curr = 1
    sum = 1
    for i in range(n - 1):
        prev, curr = curr % 10, (prev + curr) % 10
        sum += (curr % 10) ** 2
    if n % 60 == 0:
        return (sum % 10) - 1
    return sum % 10

n = int(input())
print(last_digit_sum_square(n))