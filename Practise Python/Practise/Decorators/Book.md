
# total_ordering

## Problem
1. No overloads for "sorted" match the provided arguments
  Argument types: ((book: Unknown) -> int)
```python
    [
        if __name__ == "__main__":
        book = [
            Book("The Untethered Soul", 20),
            Book("Master Your Emotions", 55),
            Book("The Concise Human Body", 100)
        ]

        sorted_book = sorted(key=lambda book: len(book)) 
        print("Sorted Book by Pages")
        for book in sorted_book:
            print(book)
    ]
```

## Reason
1. The error occurs because the `sorted` function is trying to compare two objects of different types

## Solution
1. Define `Book` class
2. Add a `__len__` method to the `Book` class to allow `len(book)` to return a value (e.g., the number of pages)
```python
    [
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
    ]
```

## Notes
1. Automatically generates __le__ (less than or equal), __gt__ (greater than), and __ge__ (greater than or equal) based on the two defined methods.
2. **@total_ordering** is to generate the missing comparison methods.

