from model import person

class Student(person.Person):
    table_name = 'student'
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        
    