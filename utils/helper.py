from models.window import Window

from datetime import datetime

from os import path


def path_exists(function):
    def checker(chosen_path):
        return path.exists
    return checker


@path_exists
def verify_file(chosen_path: str) -> bool:
    return path.isfile(chosen_path)


@path_exists
def verify_directory(chosen_path: str) -> bool:
    return path.isdir(chosen_path)
