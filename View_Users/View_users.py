import os

import Main_Code.main


def list_users_volume():
    Main_Code.main.clean_console()
    my_var = os.getenv("PYTHONPATH")

    print(f"MY_VARIABLE is: {my_var}")

    # This is the PATH inside the Docker Container Volume
    path_volume_docker = "/Docker_Directory/Storage/User_Data.txt"

    # Going one level up -> /Docker_Directory/Storage/
    directory_storage = os.path.dirname(path_volume_docker)

    # Check if the directory inside the volume exist or not.
    if not os.path.exists(directory_storage):
        print(f"The directory {directory_storage} was not found")

    # Try statesman to read all the file "USER_DATA" into the Docker volume
    try:
        with open(path_volume_docker, 'r') as storage_file:
            content = storage_file.read()
            print("List Users:", end="\n")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
