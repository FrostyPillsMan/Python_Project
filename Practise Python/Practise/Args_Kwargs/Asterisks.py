def print_genius(*names):
    print(type(names))
    for name in names:
        print(name)

print_genius('Elon Musk', 'Jeff Bezos', 'Mark Cuban', 'Adam Tan')
print("\n")

def top_entrepreneur(**names):
    print(type(names))
    for key, values in names.items():
        print(key, values)

top_entrepreneur(Top1="Elon Musk", Top2="Jeff Bezos", Top3="Adam Tan")
print("\n")

def entrepreneur(*, first_name, last_name):
    print(first_name, last_name)

# entrepreneur('Adam', 'Tan')
entrepreneur_identity = entrepreneur(first_name='Adam', last_name='Tan')

def genius(age, *, first_name, last_name):
    print(first_name, last_name, 'is', age)

genius(60, first_name='Jeff', last_name='Bezos')

A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [a for a in A] + [b for b in B] + [c for c in C]
print(L)

K = [*A, *B, C]
print(K)

