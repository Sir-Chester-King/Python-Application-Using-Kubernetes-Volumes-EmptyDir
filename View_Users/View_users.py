import os

import Main_Code.main


def list_users_volume():
    Main_Code.main.clean_console()

    # This is the PATH inside the Project Directory (current directory)
    # -> Python_App_Using_Kubernetes/Store_Data/Store_data.py
    absolutepath = os.path.abspath(__file__)

    # Go up one level -> Python_App_Using_Kubernetes/Store_Data
    one_level_up = os.path.dirname(absolutepath)

    # Go up two levels -> Python_App_Using_Kubernetes
    two_level_up = os.path.dirname(one_level_up)

    # Check if the directory inside the project exist or not.
    # In case it doesn't exist, it is created.
    directory_storage = os.path.join(two_level_up, "Storage")

    # Name of the file will contain the user's data.
    file_name = "Data_Users.txt"

    # Path of the txt file where the user's data will stored
    file_path = os.path.join(directory_storage, file_name)

    if not os.path.exists(directory_storage):
        print(f"The directory {directory_storage} was not found")

    # Try statesman to read all the file "USER_DATA" into the Docker volume
    try:
        with open(file_path, 'r') as storage_file:
            content = storage_file.read()
            print("List Users:", end="\n")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
