if __name__ != '__main__':
    def find_GCD(a, b):
        current_GCD = 1
        for d in range(2, min(a, b) + 1):
            if a % d == 0 and b % d == 0:
                current_GCD = d
        return current_GCD

    a, b = map(int, input().split())
    print(find_GCD(a, b))

if __name__ == '__main__':
    def calc_GCD(a, b):
        if b == 0:
            return a
        else:
            return calc_GCD(b, a % b)
    
    a, b = map(int, input().split())
    print(calc_GCD(a, b))