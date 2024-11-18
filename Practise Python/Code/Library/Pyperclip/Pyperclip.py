import pyperclip

try:
    print("Do something that throws error...")
    raise SyntaxError("Something went wrong...")
except Exception as e:
    pyperclip.copy(str(e))

