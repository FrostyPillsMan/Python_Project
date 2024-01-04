# format Specifier
price = 2.045545

print(f"The price is ${price:^10}")

print("-----------------------------------")

# dictionary
person = {"name": "Adam", "age": 20}

bio_details = "name is {} and age is {}".format(
    person["name"], person["age"]
)  # optional -> {0}, {1} accessing dictionary key index.
print(bio_details, "\n")

# dictionary(1)
animal = {"name": "Wolf", "breed": "Siberian Husky"}

animal_bio = "name is {0[name]} and breed is {0[breed]}".format(animal)
print(animal_bio, "\n")

animal_details = "{name} are as long as really tall people—but much faster. They are consider an {breed} in a Northern area.".format(
    **animal
)  # much more readable code.
print(animal_details)

print("----------------------------------")


# OOP
class Person:
    def __init__(self, name, place, status) -> None:
        self.name = name
        self.place = place
        self.status = status


person_id = Person("Thomas Shelby", "Birmingham", "Sigma")

biography = "{0.name} is a most dangerous gangster in the street of {0.place}. Consider him as a man of {0.status} himself.".format(
    person_id
)
print(biography, "\n")
print("-----------------------------------")




