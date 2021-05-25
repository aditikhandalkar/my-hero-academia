def find_pivot(arr):
    for i in range(len(arr)):
        if arr[i] >= arr[i + 1]:
            return (i + 1) % len(arr)


def find_sum(arr, sum):
    pivot = find_pivot(arr)
    high = pivot - 1
    low = pivot % len(arr)

    while low != high:
        # if low<pivot: break
        if arr[low] + arr[high] == sum:
            print(arr[low], arr[high])
            low = (low + 1) % len(arr)
            high = (high - 1 + len(arr)) % len(arr)

        elif arr[low] + arr[high] < sum:
            low = (low + 1) % len(arr)
        else:
            high = (high - 1 + len(arr)) % len(arr)

A = [10, 12, 13, 15, 3, 5, 6, 8, 9]
sum = 18
print(find_sum(A, sum))
