
# Programming/Python 

**What is OOP?**
- An Programming style through data structure that uses *object* and their interactions to design *applications* and *computer programs.*

- Used to build *robust* and *maintainable software.*

- Real-World Example of OOP such as **Car** & **Student** & **Bank Account**
-------------------------------------------------------------------------------------------------
**Class**
- BLueprint of an object where it holds the **data** and controls the **behavior** of presenting the model of an object.
- An **object** might be a *variable* or a *method* & an *instance* that belongs to the class afterwards. **Class** is actually an object as well.
- **Objects** encapsulate *data (attributes)* and *behavior (methods)* into a single unit.

Code Example
```python
class House:
    # Class body
    pass
```

**Notes:**
In Python, the body of a given class works as a [namespace](https://www.geeksforgeeks.org/namespaces-and-scope-in-python/) where attributes and methods live. You can only access those attributes and methods through the class or its objects.

**Variable** vs **Method**
1. **Variable**(*Attributes*)
- Defined inside a class that store all the data required to be use inside a class.
- They organize and hold data till it's being used as a *instance.*

2. **Method**
- Function that you define within a class and describes an action the method performs from the class data itself.

**Similarity**
*Attributes* & *Methods*
- Collectively referred as a **Members** of a class or an object.
- They are regard as an object which is an instance of a class.

**Functions Vs Methods**

**Function** syntax
```python
function(object)
```
**Method** syntax
```python
object.method()
```

**Figure 1**

**Quote**
…in OOP, the data is encapsulated in an object, which guarantees that the data is accessible only by the object’s methods. — **Yehonathan Sharvit**

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Self**
- reference to the current object(data) so that you can use it inside the class.
```python
class Hardware:
  hardware = ["Keyboard", "Mouse"]
	def finding_hardware(self):
		return self.hardware = True
```
------------------------------------------------------------------------------------
**Special Method**
1. **__init__()**
- *Sets initial values for the attributes.*
- *Ensures all of the attributes have the correct values when creating new instance.*

**Advantages**
1. *Makes the code more organized and easier to debug.*
------------------------------------------------------------------------------------
**Instance Attributes**
- *Variables* that holds the value, attach to a particular object of a class itself.
- *Attribute's value* containing *instance* 

**Attributes** 
- *.living_room*
- *.master_bedroom*
- *.aisle*
- *.garage*
- *.kid_room*
- *.kitchen*

**Conclusion**
- These attributes take values from the arguments to *.__init__(),* which are the arguments that will pass down to the class constructor, **House()**, to create concrete data.

**Class Attributes**
- *Variables* that holds the value, attach to the class itself.
- Using *instances* to access the class or self attributes.

**Noted**
- To modify class attribute, you need to access the attribute using **class name**.
						
------------------------------------------------------------------------------------
**Creating an Objects From a Class in Python**
- With every action of creating an concrete objects from the class, it is known as **Instantiation.**
- This result in create a new object of the target class itself.

Code Example
```python
# OOP_Practise.py
class House:
    def __init__(self, living_room):
        self.living_room = living_room
```

```python
# OOP_Practise_1.py
from OOP_Practise import House

father_room = House("TV")
father_room.living_room

print(father_room.living_room)

# Output
TV
```
							
**father_room** is an *instance* of **House**(Class (*object*))

**Problems Occur**
- Unlike *class attributes*, you can't access instance attributes through the class.

**Solution**
- Always access them through their **instance(object).**					
------------------------------------------------------------------------------------
**Accessing Attributes and Methods**
- Using **dot notation** with the **dot operator.**

**Dot** syntax
```python
obj.attribute_name
# Returns stored value in the target attribute

obj.method_name()
# Access target method so that user can call it for usable action
```

**Dot Syntax**

What does **dot(.)** represents in this scenario?
- Gives me following **attribute** or **method** from the object itself.

**Notes:** 
Remember that to call a function or method, you need to use a pair of parentheses and a series of arguments, if applicable.
------------------------------------------------------------------------------------
## Reference
1. https://realpython.com/python-classes/
2. https://realpython.com/quizzes/python-classes-oop/
3. https://mathspp.com/blog/pydonts/describing-descriptors#:~:text=Descriptors%2C%20like%20properties%2C%20let%20you,%2C%20setter%2C%20and%20deleter%20methods
4. 

