def coveringSegments(seg_list):
    right_end = [seg_list[0][1]]
    number_of_points = 1
    for i in range(1, len(seg_list)):
        if seg_list[i][0] <= right_end[-1]:
            if i == len(seg_list) - 1:
                break
            continue
        right_end.append(seg_list[i][1])
        number_of_points = number_of_points + 1

    print(number_of_points)
    for i in right_end:
        print(i, end=" ")

if __name__ == '__main__':
    n = int(input())
    segment_list = []

    for i in range(n):
        a, b = map(int, input().split())
        segment_list.append((a,b))

    segment_list.sort(key=lambda x: x[1])

    coveringSegments(segment_list)