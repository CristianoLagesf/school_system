from utils import functions
from control.menu_control import students_menu_controller

def students_menu():
    functions.clear_view()
    print("====================================")
    print("Manage Students")
    print("====================================")
    
    print("Please choose an option: \n")
    
    print("[1] Add Student")
    print("[2] Edit Student")
    print("[3] Remove Student")
    print("[4] List All Students")
    print("[5] Search Student by Name/ID")
    print("[0] Back to Main Menu")
    print("\n")
    
    print("(Type the number of the option and press ENTER)")
    option = int(input("Option: "))
    students_menu_controller.menu_controller(option)
    