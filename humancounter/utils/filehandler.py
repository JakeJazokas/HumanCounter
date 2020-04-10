import os

def fetch_file_path(directory, file_name):
    return os.path.join(os.path.dirname(directory), file_name)