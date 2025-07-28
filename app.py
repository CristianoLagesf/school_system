from view import main_menu
from model import database
from control.menu_control import main_menu_controller


main_menu.menu()
database.init_db()
option = int(input("Option: "))

main_menu_controller.menu_controller(option)