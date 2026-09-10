#Многопоточная быстрая сортировка
import threading
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def threaded_quicksort(arr, result):
    result.extend(quicksort(arr))

data = [random.randint(0, 100) for _ in range(10)]
result = []

thread = threading.Thread(target=threaded_quicksort, args=(data, result))
thread.start()
thread.join()

print(f"Original: {data}")
print(f"Sorted: {result}")
