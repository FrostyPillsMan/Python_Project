from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    gender: str
        
def main() -> None:
    person = Person(name="Adam", gender="Male")
    print(person)

if __name__ == "__main__":
    main()

