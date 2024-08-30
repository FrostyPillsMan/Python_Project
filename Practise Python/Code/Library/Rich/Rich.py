from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table


# Create text
writing_text = "Ordinary man with an exceptional ability"

# Create code
code = '''# include <iostream>
# using namespace std;

int main() {
    cout<<"Welcome to the C++ Language!!!";
}

return 0;
'''

# Create table
table = Table(show_header=True, header_style="bold cyan")

# Add columns
table.add_column("ID")
table.add_column("Name")
table.add_column("Age")

# Add rows
table.add_row("1", "Adam", "21")
table.add_row("2", "Nhi", "25")
table.add_row("3", "Thomas", "30")


# Create syntax
syntax = Syntax(code, "c++", line_numbers=True, theme="github-dark")

# Create console
console = Console()

# Print highlighted syntax
console.print(syntax)

# Print highligted table
console.print(table)

