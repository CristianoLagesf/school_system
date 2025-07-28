from control.logic_control import logic_student

def menu_controller(option):
    match option:
        case 1:
            logic_student.create_student()
        case 2:
            logic_student.update_student()
        case 3:
            logic_student.delete_student()
        case 4:
            print("progressss")
        case 5:
            print("progressss")
        case 6:
            print("progressss")
        case 7:
            print("progressss")
        case 0:
            print("progressss")
        case _:
            print("progressss")