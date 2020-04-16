if __name__ != '__main__':
    def calc_lcm(a,b):
        for i in range(max(a, b), a*b + 1):
            if i % a == 0 and i % b == 0:
                return i

    a, b = map(int, input().split())
    print(calc_lcm(a,b))

if __name__ == '__main__':
    def calc_hcf(a, b):
        if b == 0:
            return a
        else:
            return calc_hcf(b, a % b)

    def calc_lcm(a, b):
        return int(a*b / calc_hcf(a, b))

    a, b = map(int, input().split())
    print(calc_lcm(a,b))