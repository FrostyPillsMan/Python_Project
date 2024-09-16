
# Programming/Python 

**Benefits of Using Classes in Python**
- *Model and solve complex real-world problems*
- *Reuse code and avoid repetition*
- *Encapsulate related data and behaviors in a single entity*
- *Abstract away the implementation details of concepts and objects*
- *Unlock polymorphism with common interfaces(interaction between two objects)*
----------------------------------------------------------------------------------------------------------------------------------------------------------
**Best time to avoid using Classes**
- *Store only data* --> Use **data class** or **named tuple**
- *Provide single method* --> Use a **function**

> **"Simple is better than Complex"**

***Classes aren't necessary to work with five scenarios:***
- A small and **simple program** or **script** that doesn’t require complex data structures or logic. In this case, using classes may be overkill.
- A **performance-critical** program. Classes add overhead to your program, especially when you need to create many objects. This may affect your code’s general performance.
- A **legacy codebase**. If an existing codebase doesn’t use classes, then you shouldn’t introduce them. This will break the current coding style and disrupt the code’s consistency.
- A team with a **different coding style**. If your current team doesn’t use classes, then stick with their coding style. This will ensure consistency across the project.
- A codebase that uses **functional programming**. If a given codebase is currently written with a **functional** approach, then you shouldn’t introduce classes. This will break the underlying coding paradigm.
-------------------------------------------------------------------------------------------------
**Special Method**
**vars()**
- Returns a dictionary of all the members associated with the object.
**.__dict__**
- Access the value of *Class attribute name* in dictionary format
- Contain members of the **Class** **Attribute** or **Methods**

```python
# OOP_Practise.py
class House:
    house_prices = 100.29

    def __init__(self, living_room):
        self.living_room = living_room
```
		
```python
# OOP_Practise_1.py
print(House.__dict__)
print(House.__dict__["house_prices"])
# 100.29
```
											
**Note:**
You can access the same dictionary by calling the built-in **vars()** function on your class or instance, as you did before.

**Accessing Instance Attributes**
```python
# Instance Attributes
class Shop:
    shirt_prices = 12.99

    def __init__(self, tag, colour) -> None:
        self.tag = tag
        self.colour = colour
        self.shirt = Shop.shirt_prices
        Shop.shirt_prices += 3.99


s1 = Shop("Shirt", "Black")
print(s1.shirt) # 12.99
print(s1.__dict__) # {'tag': 'Shirt', 'colour': 'Black', 'shirt': 12.99}
print(s1.__dict__["shirt"])  # 12.99
shirt_display = s1.__dict__["shirt"] = "Shirt", "Red"
print(shirt_display)  # ('Shirt', 'Red')
```


