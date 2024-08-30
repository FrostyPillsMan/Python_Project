import rich
from rich.console import Console
from rich.tree import Tree
from rich.markdown import Markdown


rich.print(":smiley: Hello Rich! :thumbs_up::money_with_wings:")

warning_message = ":warning: Warning: Unauthorized access detected!"
rich.print(warning_message)

# Create a tree structure
tree  = Tree("Root")
tree.add("child1 :child:")
tree.add("child2 :child_dark_skin_tone:")

child3 = tree.add("child3 :child_medium-light_skin_tone:")
child3.add("grandchild1 :child:")

tree.add("child4 :child_medium-dark_skin_tone:")

# Markdown text

markdown_text = """
# My Markdown Document

This is a **Markdown** document that will be displayed in the console output.

## Section 1

This is the *first* section of the document. It contains a list:

* Item 1
* Item 2

## Section 2

This is the second section of the document. It contains a code block:

```python
print("Python")
```
"""


# Convert the Markdown to a Rich object
markdown_display = Markdown(markdown_text)

# Create console
console = Console()

# Print tree
console.print(tree)

# Print the Markdown
console.print(markdown_display)

