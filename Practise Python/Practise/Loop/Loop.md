
# Loop🌀

## Iterables
1. an object of capable **returning its members one by one.**

**Sequences**
1. type of iterable such as **lists**, **strings**, **tuples**

```python
    [
        numbers = [10, 12, 15, 18, 20]
        fruits = ("apple", "pineapple", "blueberry")
        message = "I love Python ❤️"
    ]
```
---
## Other Iterables
1. **Dictionaries**, **file objects**, **sets**, and **generators** are all iterables, but none of them is a sequence.

```python
    [
        my_set = {2, 3, 5}
        my_dict = {"name": "Ventsislav", "age": 24}
        my_file = open("file_name.txt")
        squares = (n**2 for n in my_set)
    ]
```
---
## Python’s for loops don’t use indices

```python
    [
        `while loop`(Sequences-Object)

        index = 0
        numbers = [1, 2, 3, 4, 5]
        while index < len(numbers):
        print(numbers[index])
        index += 1

        # 1 2 3 4 5

        `while loop`(Non-Sequences-Object)

        index = 0
        numbers = {1, 2, 3, 4, 5}
        while index < len(numbers):
        print(numbers[index])
        index += 1
        
        # TypeError: 'set' object is not subscriptable

        `Alternatives --> for loop`
        numbers = {1, 2, 3, 4, 5}
        for number in numbers:
        print(number)

        # 1 2 3 4 5
    ]
```
---
## Additional Notes On Iterators
1. An **iterable** is something you can loop over
2. An **iterator** is an object representing **stream of data.** It does the **iterating** over an iterable.

## Benefits Of Iterators
- Save us lof of **memory** and **CPU time**

## Iterators are everywhere
1. Enumerate
2. Reversed
3. Zip
4. Map
5. Filter
6. File Objects
7. Dictionary
8. Data Science --> Large Datasets

## References
1. *Basics-Iteration-And-Looping:*[TowardsDataScience](https://towardsdatascience.com/python-basics-iteration-and-looping-6ca63b30835cs)

