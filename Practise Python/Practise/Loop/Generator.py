def gen1():
    yield "I am the bone of my sword"
    yield "Steel is my body and fire is my blood"
    yield "I have created over a thousand blades"


temp_gen1 = gen1()
# print(next(temp_gen1))
# print(next(temp_gen1))
# print(next(temp_gen1))

for value in enumerate(temp_gen1, start=1):
    print(value)

