from model import person

class Professor(person.Person):
    table_name = 'professor'
    def __init__(self, name, idade, id):
        super().__init__(name, idade, id)