import os.path

from server.common.exceptions import FileNotFoundException


def check_path_exists(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundException(f"File {path} not found")
    return path
