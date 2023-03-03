class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def hello(self):
        print(f"Hello my name is {self.name}")

    @classmethod
    def role(cls):
        if (cls.__name__ == "Student"):
            return "Student"
        else:
            return "Professor"

    @staticmethod
    def stati_info():
        info = """
            Name: person
            Surname: person
            Age: 0"""

        return info

    def __add__(self, other):
        return self.name + " study with " + other.name