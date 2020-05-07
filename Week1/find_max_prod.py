if __name__ == '__main__':
    def find_max_prod(list_of_numbers):
        n = len(list_of_numbers)
        max_index1 = -1
        for i in range(n):
            if max_index1 == -1 or list_of_numbers[i] > list_of_numbers[max_index1]:
                max_index1 = i
        max_index2 = -1
        for i in range(n):
            if i != max_index1 and (max_index2 == -1 or list_of_numbers[i] > list_of_numbers[max_index2]):
                max_index2 = i
        return list_of_numbers[max_index1] * list_of_numbers[max_index2]

    number = int(input())
    list_of_numbers = list(map(int, input().split()))
    print(find_max_prod(list_of_numbers))