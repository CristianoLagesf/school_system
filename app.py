from view import main_menu
from control.menu_control import main_menu_controller


main_menu.menu()
option = int(input("Option: "))
main_menu_controller.menu_controller(option)