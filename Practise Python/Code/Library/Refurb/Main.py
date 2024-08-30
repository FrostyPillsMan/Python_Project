from pathlib import Path
import os

filenames = ("./Practise Python/Code/Refurb/Pokemon.txt")

# my python file content
for filename in filenames:
    try:
        file_contents = Path(filename).read_text()
        file_lines = file_contents.splitlines()
        print(file_contents)

        for line in file_lines:
            # Skip empty lines and comments
            if not line or line.startswith(("#", "// ")):
                continue

        # Split the lines into words and print each word
        for word in line.split(): # Correctly splitting the line
            print(f"[{word}]", end="")  
        print() # print a newline after each line of words

    except FileNotFoundError:
        print(f"Error: The file '{filenames}' was not found...")
        break
    except PermissionError:
        print(f"Error: Permission denied for file '{filenames}'.")
    else:
        print(f"{filenames} has been founded...")
    finally:
        print(f"Current Working Directory: {os.getcwd()}", end="\n")
        print("The file has been executed correctly...")

