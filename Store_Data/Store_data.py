# This function store the personal user's data in a file.
# The path of the file will be inside the project's directory.
import os


def Store_Data_Into_Volume(user):
    # This is the PATH inside the Docker Container Volume
    path_volume_docker = "/Docker_Directory/Storage/User_Data.txt"

    # Check if the directory inside the volume exist or not.
    # In case it doesn't exist, it is created.
    directory_storage = os.path.dirname(path_volume_docker)

    # Check if the "Storage" directory exist, in case it does not exit, it created.
    if not os.path.exists(directory_storage):
        os.makedirs(directory_storage)
        print(f"Created directory: {directory_storage}")

    # Writing the data in the file.
    try:
        with open(path_volume_docker, 'a+') as storage_file:
            storage_file.write(f"Name: {user.get_name()}\n")
            storage_file.write(f"Surname: {user.get_surname()}\n")
            storage_file.write(f"Address: {user.get_address()}\n")
            storage_file.write(f"Phone Number: {user.get_phone_number()}\n\n")
    except FileNotFoundError:
        with open(path_volume_docker, 'w+') as storage_file:
            storage_file.write(f"Name: {user.get_name()}\n")
            storage_file.write(f"Surname: {user.get_surname()}\n")
            storage_file.write(f"Address: {user.get_address()}\n")
            storage_file.write(f"Phone Number: {user.get_phone_number()}\n\n")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
