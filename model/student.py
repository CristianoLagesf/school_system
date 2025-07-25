from person import Person

class Student(Person):
    def __init__(self, name, idade, id):
        super().__init__(name, idade, id)