from functools import total_ordering

@total_ordering
class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page

    def __eq__(self, other):
        # checks if two attributes have the same priorities.
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.page

    def __lt__(self, other):
        # checks if one book has a lower priority than another.
        if not isinstance(other, Book):
            return NotImplemented
        return self.page < other.page

    def __len__(self):
        return self.page

    def __str__(self):
        return f"{self.title}: {self.page} pages"


if __name__ == "__main__":
    books = [
        Book("The Untethered Soul", 20),
        Book("Master Your Emotions", 55),
        Book("The Concise Human Body", 100)
    ]

    sorted_book = sorted(books, key=lambda book: len(book)) 
    print("Sorted Book by Pages📖📄")
    for book in sorted_book: 
        print(book)

