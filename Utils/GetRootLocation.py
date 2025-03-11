import os


def get_root_location():
    current_script_path = os.path.abspath(__file__)  # Get the absolute path of the current script
    root_location = os.path.dirname(os.path.dirname(current_script_path))  # Go up two levels to the project root
    return os.path.normpath(root_location)



