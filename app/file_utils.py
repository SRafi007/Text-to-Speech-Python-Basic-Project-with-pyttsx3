import os

def validate_file_path(file_path: str) -> bool:
    return os.path.isfile(file_path)

def create_output_directory(directory_path: str):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
