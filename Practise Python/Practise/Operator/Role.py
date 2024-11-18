# Simplify while loops
file = open("./Practise Python/Practise/Operator/Role.txt", "r")
while content_line := file.readlines():
    print(content_line)

# Streamline if conditions
if (p := input("Enter the password: ")) == "Adam's password":
    login('Adam', p)

