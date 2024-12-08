def binary_search(List, n):
    low = 0
    high = len(List) - 1
    while low <= high:
        mid = (low + high) // 2
        if List[mid] == n:
            return mid
        elif List[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return None


List = [1, 3, 5, 7, 9, 11, 13, 44, 65, 87]
n = int(input("Enter the number: "))

Result = binary_search(List, n)

if Result is not None:
    print(f"Entered number {n} is found at {Result + 1}")
else:
    print(f"Entered number {n} is not found")
