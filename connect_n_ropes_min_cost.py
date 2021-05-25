import heapq
from heapq import heappush, heappop


def connect_n_ropes_min_cost(arr):
    heapq.heapify(arr)

    cost = 0
    while len(arr)>1:

        x = heappop(arr)
        y = heappop(arr)

        sum = x + y

        heappush(arr, sum)
        cost += sum

    return cost

arr = [5, 4, 2, 8]
cost = connect_n_ropes_min_cost(arr)
print(cost)
