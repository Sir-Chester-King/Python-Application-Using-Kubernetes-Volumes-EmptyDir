# Main function of program.
# The purpose of this application is to create objects "user" and store their info's in a file.
import os

import Create_Users.Create_users
import View_Users.View_users


def clean_console():
    # For Windows environment
    if os.name == 'nt':
        os.system('cls')
    # For Linux/Unix environment
    else:
        os.system("clear")


def main():
    menu_app = {
        "1": "Create new user",
        "2": "View list users"
    }
    options_available = list(menu_app.keys())

    # Print the menu app as readable for users.
    print("{:<10} {:<15}".format('Option', 'Action'))
    for key, value in menu_app.items():
        print("{:<10} {:<15}".format(key, value))
    print("Please, insert only the available value from the menu.")

    # Loop state in case of wrong input option insert
    option_chosen = str(input("Insert option: "))
    while option_chosen not in options_available:
        option_chosen = str(input("Insert option: "))

    clean_console()

    # Call the property function based on the user's chosen option.
    match option_chosen:
        case "1":
            Create_Users.Create_users.new_user()
        case "2":
            View_Users.View_users.list_users_volume()
        case _:
            return 0


# __name__ is a special built-in variable that exists in every module (a module is simply a Python file).
# __main__ is a string that Python assigns to the __name__ variable when the module is executed as the main program.
# It serves as an entry point for the script execution.
# The if __name__ == "__main__": condition checks whether the script is being run directly or being imported.
# Code inside this if block will only execute if the script is run directly, not when it is imported.
if __name__ == "__main__":
    main()
