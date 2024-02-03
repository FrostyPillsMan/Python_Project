def create_soldiers(person):
    if person.startswith("A"):
        return person
    return person is None


person = ["Adam", "Audrey", "Aidren", "Bitches", "Hinko"]

person_abstract = list(map(create_soldiers, person))
print(person_abstract)

# ['Adam', 'Audrey', 'Aidren', False, False]

print("-----------------------------------------------------------------")


citizens = [("John", 10), ("Adam", 3), ("Audrey", 78)]


def tax(citizen):
    name = citizen[0]
    taxed_balance = citizen[1] * 0.93
    return (name, taxed_balance)


taxed_citizens = list(map(lambda c: (c[0], c[1]*0.93), citizens))
# taxed_citizens = [(name, money*0.93) for name, money in citizens]
# taxed_citizens = [tax(citizen) for citizen in citizens]

print(taxed_citizens)
# [('John', 9.3), ('Adam', 2.79), ('Audrey', 72.54)]


