from person import Person

class Professor(Person):

    university = 'La Sapienza' # class attribute
    role = 'professor' # class attribute

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age) # call superclass constructor

    def print(self):
        data = f'Name: {self.name}\nSurname: {self.surname}'
        print(data)