data = [1, {"a": 2, "b": 3.5}, {"c": 4}, 10]


def process_data(data):
    result = []
    for item in data:
        if not isinstance(item, dict):
            continue
        for key, value in item.items():
            if not isinstance(value, (int, float)):
                continue
            result.append(value * 2)
    return result


data_exec = process_data(data)
print(data_exec)

