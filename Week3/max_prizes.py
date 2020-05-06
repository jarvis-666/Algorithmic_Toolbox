def max_prizes(n):
    k = 0     # number of places that have been awarded candies
    i = 1      # iterative variable to distribute candies
    candies_given = [0]
    if n == 1 or n == 2:
        k = 1
        candies_given.append(n)
        print(k)
        print(candies_given[-1])

    if n > 2:
        while n > candies_given[-1]:
            n -= i
            k += 1
            candies_given.append(i)
            i += 1

        if n <= candies_given[-1]:
            candies_given[-1] += n
            print(k)
            for i in range(1, len(candies_given)):
                print(candies_given[i], end=" ")


if __name__ ==  "__main__":
    n = int(input())
    max_prizes(n)