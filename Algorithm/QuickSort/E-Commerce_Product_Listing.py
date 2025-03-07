# Scenario: Sorting E-commerce Product Listings by Price

from pprint import pprint

products = [
    {"product_id": 1, "name": "Phone", "price": 699},
    {"product_id": 2, "name": "Laptop", "price": 999},
    {"product_id": 3, "name": "Headphones", "price": 199},
    {"product_id": 4, "name": "Tablet", "price": 499},
]

def quicksort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[key] < pivot[key]]
    middle = [x for x in arr if x[key] == pivot[key]]
    right = [x for x in arr if x[key] > pivot[key]]
    return quicksort(left, key) + middle + quicksort(right, key)

# Sorting products by price
sorted_products = quicksort(products, "price")
pprint(sorted_products)

