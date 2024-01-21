class Student:
    num_undergraduates = 0
    num_postgraduates = 0

    undergraduates_age_range = range(19, 24)
    postgraduates_age_range = range(24, 30)

    def __init__(self, _id, first_name, last_name, age, first_name_first=True) -> None:
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.first_name_first = first_name_first
        self.age = age

        if self.age in Student.undergraduates_age_range:
            Student.num_undergraduates += 1
        elif self.age in Student.postgraduates_age_range:
            Student.num_postgraduates += 1
        else:
            raise Exception("Invalid Age")

        self.classes = []

    # Getter method
    def get_full_name(self):
        if self.first_name_first:
            return self.first_name + " " + self.last_name
        else:
            return self.last_name + " " + self.first_name

    # Setter method
    def set_full_name(self, full_name):
        if self.first_name_first:
            self.first_name, self.last_name = full_name.split()
        else:
            self.last_name, self.first_name = full_name.split()

    # Delete method
    def delete_full_name(self):
        print("I am deleter")
        self.first_name = None
        self.last_name = None

    full_name = property(get_full_name, set_full_name, delete_full_name)

   
student1 = Student(1, "Jack", "Ma", 24, first_name_first=False)
print(student1.get_full_name())
print(student1.full_name)

student2 = Student(1, "Jac", "John", 25, first_name_first=True)

print("Before...")
print(student2.first_name)
print(student2.last_name)
print(student2.full_name)

print("\nAfter...")
student2.full_name = "John Doe"
print(student2.first_name)
print(student2.last_name)
print(student2.full_name)

student3 = Student(1, "Jac", "John", 25, first_name_first=False)

print("\nBefore...")
print(student3.first_name)
print(student3.last_name)
print(student3.full_name)

print("\nAfter...")
del student3.full_name
print(student3.first_name)
print(student3.last_name)



