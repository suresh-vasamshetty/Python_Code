def sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                # temp = list[j + 1]
                # list[j + 1] = list[j]
                # list[j] = temp
                list[j], list[j + 1] = list[j + 1], list[j]

list = [3, 6, 2, 7, 9, 1, 8]
sort(list)

print(list)
