def isGreaterOrEqual(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    fnum1 = num1 + num2
    fnum2 = num2 + num1
    if fnum1 >= fnum2:
        return True

def max_sal(list1):
    answer = []
    while len(list1) != 0:
        max_digit = -1
        for digit in list1:
            if isGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        list1.pop(list1.index(max_digit))
    return answer

if __name__ == '__main__':
    n = int(input())
    list_of_numbers = list(map(int, input().split()))
    result = max_sal(list_of_numbers)
    for i in result:
        print(i, end="")