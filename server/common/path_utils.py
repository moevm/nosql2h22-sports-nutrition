import os.path

from server.common.exceptions import FileNotFound


def check_path_exists(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFound(f"File {path} not found")
    return path
