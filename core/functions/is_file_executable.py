import os


def is_file_executable(file_path: str) -> bool:
    """
    Returns True if given file is executable.
    This function works only in 'posix' environment.
    :param file_path: Path to file including filename.
    :return: True is file is executable, False otherwise.
    """
    is_file = os.path.isfile(file_path)
    is_executable = os.access(file_path, os.X_OK)
    return is_file and is_executable
