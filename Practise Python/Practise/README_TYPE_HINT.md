
# Type Hint😉

# What is **Type Hint** 
- Indicates types of **variables** && **function parameters** && **return values.**
- Help developers to know the use of your **data type** from the **function which will expects to return the expected value of a function itself.** 

# Benefit of Type Hint
1. **More readable for other developers**
2. **Type safer to avoid hard-to-find bugs**
3. **Provide more information for modern IDEs' automatic code completion**
4. **IDEs' can help you check the potential bugs with the help of the type hints**
5. **Makes your programming life easier**


# Extra Resources(Reference)
- `https://mypy.readthedocs.io/en/stable/runtime_troubles.html#using-new-additions-to-the-typing-module`
- `https://dagster.io/blog/python-type-hinting`
----------------------------------------------------------------------------------------------
# Mistakes Learn😦

# Error on code review
- def apply_message(message: message_Function, a: str) -> str:
      return message(message_Function, a)

    # Reason
    - TypeError: receive_message() takes 1 positional argument but 2 were given (Output)

# Solution 
- def apply_message(message: message_Function, a: str) -> str:
      return message(a)

    # Expected Result
    -  Message arrival:  Hello (Output)


# Error on Static-Type Checker(Mypy)
- def apply_message(message: message_Function, a: str) -> str:
      return message(a)

  def receive_message(call: str) -> str:
      return call

message_appear = apply_message(receive_message, "Hello")
print("Message arrival: ", message_appear)

# Reason 
1. The apply_message function expects two arguments: **message** (which is a function taking two strings and returning a string) and **a** (which is a string). However, when it's called in message_appear = apply_message(receive_message, "Hello"), it only passes receive_message as the first argument and "Hello" as the second argument, leading to a Too few arguments  [call-arg].
2. The receive_message function takes one argument call, which aligns with the signature Callable[[str], str]. However, apply_message expects a function that takes two strings, as indicated by the error: "Argument 1 to **apply_message** has incompatible type "Callable[[str], str]"; expected "Callable[[str, str], str]"" [arg-type].
3. Found 2 errors in 1 file (checked 1 source file)

# Solution 
message_Function = Callable[[str, str], str]

def apply_message(message: message_Function, a: str) -> str:
    return message(a, "Goodbye!")

def receive_message(call: str, another_call: str) -> str:
    return call + " " + another_call

message_appear = apply_message(receive_message, "Hello")
print("Message arrival: ", message_appear)

# Expected Result 
- Success: no issues found in 1 source file
----------------------------------------------------------------------------------------------
# Lesson Notes

**Literal** VS **Final**

1. **Literal**
- act as a actual fixed value that you can write down. 
- It's like an immutable data type where it restrict value to a specific set of cosntant value.

2. **Final**
- act as a constant value that you cannot reassigned after its initial name assignment.
----------------------------------------------------------------------------------------------
**Any**

1. Accepts any types of values.
2. Disable Static Type Checking where no **warnings** or **errors** appear.
3. included in Dynamic Typing.

# When using Any
1. When Static codebase involve correlated with dynamic typing
2. Not clear on what exact type to declare the variable in advance
---------------------------------------------------------------------------------------------
# Type Checkers
- Ensure that you using **variables** && **functions** in your code correctly.

**Mypy** 
- **Static type checker** in Python

# Usages
- find bugs in the programs without running them!


