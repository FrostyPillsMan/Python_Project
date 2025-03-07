# Task Scheduling in a Cloud Server

from pprint import pprint

tasks = [
    {"task_id": 1, "priority": 3, "timestamp": "2025-01-07T10:00:00"},
    {"task_id": 2, "priority": 1, "timestamp": "2025-01-07T10:01:00"},
    {"task_id": 3, "priority": 2, "timestamp": "2025-01-07T10:02:00"},
    {"task_id": 4, "priority": 4, "timestamp": "2025-01-07T10:03:00"},
]


def heapify(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][key] > arr[largest][key]:
        largest = left

    if right < n and arr[right][key] > arr[largest][key]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)


def heap_sort(arr, key):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key)

    return arr


# Sorting tasks by priority (highest first)
sorted_tasks = heap_sort(tasks, "priority")
pprint(sorted_tasks)

