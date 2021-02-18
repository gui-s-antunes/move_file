# from models.window import Window

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
