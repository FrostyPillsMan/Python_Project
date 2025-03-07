# Processing Large Log Files for Analytics

from pprint import pprint

logs_server1 = [
    {"timestamp": "2025-01-07T10:00:00", "message": "Server 1 started"},
    {"timestamp": "2025-01-07T10:01:00", "message": "Task A completed"},
]

logs_server2 = [
    {"timestamp": "2025-01-07T10:00:30", "message": "Server 2 initialized"},
    {"timestamp": "2025-01-07T10:02:00", "message": "Task B completed"},
]


def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Merging and sorting logs
all_logs = logs_server1 + logs_server2
sorted_logs = merge_sort(all_logs, "timestamp")
pprint(sorted_logs)
