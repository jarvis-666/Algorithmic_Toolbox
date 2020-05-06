def calc_change(m):
    number = 0
    while m != 0:
        if m >= 10:
            m = m - 10
            number = number + 1
        if m >= 5 and m < 10:
            m = m - 5
            number = number + 1
        if m >= 1 and m < 5:
            m = m - 1
            number = number + 1
    return number

if __name__ == '__main__':
    m = int(input())
    print(calc_change(m))