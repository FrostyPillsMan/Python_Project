def generate_fruit():
    yield 'apple'
    yield 'orange'
    yield 'pear'

for fruit in generate_fruit():
    print(fruit)

