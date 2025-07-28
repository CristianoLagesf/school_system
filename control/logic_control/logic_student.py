from model import student

def create_student():
    print("=============================")
    print("STUDENT REGISTRATION")
    print("=============================")
    
    print("Please enter the following information:")
    
    name = input("Name: ")
    age = int(input("Age: "))
    student.Student.create(name,age)

def update_student():
    print("=============================")
    print("STUDENT REGISTRATION")
    print("=============================")
    
    print("Please enter the following information:")
    
    id = int(input("Student ID: "))
    name = input("Name: ")
    age = input("Age: ")
    
    if name == '':
        student.Student.update(id,int(age))
    elif age == '':
        student.Student.update(id,name)
    else:
        student.Student.update(id,name,age)
    
def delete_student():
    print("=============================")
    print("STUDENT REGISTRATION")
    print("=============================")
    
    print("Please enter the following information:")
    
    id = int(input("Student ID: "))
    student.Student.delete(id)