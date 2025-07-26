from view import students_menu,courses_menu,enrollment_menu,professors_menu

def menu_controller(option):
    match option:
        case 1:
            students_menu.students_menu()
        case 2:
            professors_menu.professors_menu()
        case 3:
            courses_menu.courses_menu()
        case 4:
            enrollment_menu.enrollment_menu()
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