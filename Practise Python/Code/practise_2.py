import json
# import pprint

items = json.loads('[{"id": 1, "text": "Item1"}, {"id":2, "text": "Item2"}]')

for item in items:
    print(item["text"])


def run(number):
    return number

numbers = [1, 2, 3, "123", 32, "Like", [1, 3, 5]]

result = list(filter(lambda x: isinstance(x, int), numbers)) 
print(run(result))
 

# pprint.pprint(dir(json))




