def print_diamonds(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i -1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def print_hollow_square(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * rows)
        else:
            print("*" + " " * (rows - 2) + "*")

def print_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)


print_hollow_square(5)
print_diamonds(5)
print_inverted_triangle(5)

