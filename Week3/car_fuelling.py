def car_fuel(d, m, n, stops):
    currentRefill = 0       # index contains the current fuel stop
    numberRefills = 0       # contains the number of refills during trip
    while currentRefill < n - 1:   # loop till end not reached
        lastRefill = currentRefill
        while currentRefill < n - 1 and stops[currentRefill + 1] - stops[lastRefill] <= m:    # until travelled till farthest reachable station
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:         # if car did not move
            return -1
        if currentRefill < n - 1:      # if reached the farthest reachable station and still destination not reached
            numberRefills += 1
    return numberRefills

if __name__ == '__main__':
    d = int(input())        # distance between two cities
    m = int(input())        # max distance in full tank
    n = int(input())        # number of stops
    stops = list(map(int, input().split()))     # distances of refill stations from start
    stops.insert(0, 0)
    stops.append(d)
    # print(stops)
    print(car_fuel(d, m, len(stops), stops))