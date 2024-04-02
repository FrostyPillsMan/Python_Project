from functools import reduce

# Scenario 1 (Map)
def add_op(x):
    return x+5

score_1 = [10, 2, 4, 5, 6, 7]
result = set(map(add_op, score_1))
print(f"{result= }", "\n")

# Scenario 2 (Filter)
even_scores = list(filter(lambda x: (x%4 == 0), score_1))
print(f"{even_scores= }", "\n")

# Scenario 3 (Reduce)
scores = [10, 9, 8, 7, 6, 5]
new_scores = reduce((lambda x,y: x+y), scores)
print(f"{new_scores= }") 

