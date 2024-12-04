a, b, c = 10, 5, 3

print(a, b, c, sep="\n")

# Iterable Filters
list_of_peolpe = ["Adam", "Than", "Aiman", "Vincent", "Akio", "Like"]
for person_name in filter(lambda name: name.startswith("A"), list_of_peolpe):
    print(person_name)

# Sorting Dictionaries
my_dict = {'A': 2, 'B': 56, 'C': 0, 'D': 100, 'E': 8}
my_sorted_dict = sorted(my_dict.items(), key=lambda item: item[1])
print(my_sorted_dict)

