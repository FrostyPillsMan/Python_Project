# Scenario 1

friends = [
    ("Adam", 20),
    ("Bob", 20),
    ("Charlie", 25),
    ("Jim", 29),
    ("Gun", 26),
    ("Fallon", 34),
]

age = lambda data: data[1] >= 21

drinking_bros = dict(filter(age, friends))
print(drinking_bros)

print("\n##################################")

# Scenario 2
avail_hardware_parts = {
    "Multics Computer": {"Keyboard": 300, "Mouse": 400, "Headphones": 350},
    "AfterShock PC": {"Keyboard": 700, "Mouse": 800, "Headphones": 750},
    "Techfix Malaysia": {"Keyboard": 800, "Mouse": 900, "Headphones": 550},
}

keyboard_cheap = list(
    filter(lambda data: data[1]["Keyboard"] > 600, avail_hardware_parts.items())
)
keyboard_cheap_value = [
    (company, avail_parts["Keyboard"]) for company, avail_parts in keyboard_cheap
]

print(keyboard_cheap_value, "\n")

# Scenario 3
def is_prime(nums):
    if nums <= 1:
        # 1 is not a prime number.
        return False
    for x in range(2, int(nums / 2) + 1):
        # If num is divisible by any number between
        # 2 and nums / 2, it is not prime
        if (nums % x) == 0:
            # nums is not a prime number.
            return False
    return True


nums = range(1, 100)
filter_prime_data = list(filter(is_prime, nums))
print(filter_prime_data)
