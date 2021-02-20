from datetime import datetime
from functools import wraps
from os import path


# Tentar ver se dá pra fazer começar aqui, trazendo a função desejada nos parametros.
def path_exists(function):
    @wraps(function)
    def checker(chosen_path):
        """It Verifies whether argument is a valid path"""
        if path.exists(chosen_path):
            return function(chosen_path)
        else:
            return False
    return checker


@path_exists
def verify_file(chosen_path: str) -> bool:
    """Return whether the string is a file"""
    return path.isfile(chosen_path)


@path_exists
def verify_directory(chosen_path: str) -> bool:
    """Return whether the string is a directory"""
    return path.isdir(chosen_path)


def get_time() -> str:
    """Return time (string) with format: dd-mm-yy_h-m-s"""
    time_now = datetime.now()
    return time_now.strftime('%b-%d-%Y_%H-%M-%S')


def user_action(direc: str, files: list) -> int:
    """
    It checkes whether directory got a path and files got at least 1 path
    :param direc: string with a path (or empty)
    :param files: list with pathes (or empty)
    :return: A number that we choice to allow clear or aplly and clear buttons
    """
    if bool(direc) and bool(files):
        return 2
    elif bool(direc) or bool(files):
        return 1
    else:
        return 0

