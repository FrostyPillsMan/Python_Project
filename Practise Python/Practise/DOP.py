from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class AuthorData:
    """Class for keeping track of the author records in the system."""

    first_name: str
    last_name: str
    n_books: int


def calculate_name(first_name: str, last_name: str):
    return f"{first_name} {last_name}"


def is_prolific(n_books: int):
    return n_books > 100


author_data = AuthorData("Muhammad", "Adam", 90)
print(calculate_name(author_data.first_name, author_data.last_name))
print(is_prolific(author_data.n_books))
print(asdict(author_data))

print("------------------------------------------------------------")


class Address:
    def __init__(
        self, street_num: int, street_name: str, city: str, state: str, zip_code: int
    ):
        self.street_num = street_num
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Author:
    def __init__(self, first_name: str, last_name: str, n_books: int, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.n_books = n_books
        self.address = address

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_prolific(self):
        return self.n_books > 100


address = Address(651, "Essex Street", "Brooklyn", "NY", 2084)
author = Author("Adam", "Tan", 200, address)
assert author.full_name == "John Cena", "Wrong name"
print(author.full_name)
print(author.is_prolific)


"""Extra Resources
https://towardsdatascience.com/data-oriented-programming-with-python-ef478c43a874
"""
