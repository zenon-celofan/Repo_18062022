import os


def get_file_size(file_path: str) -> int:
    """
    Returns file size from given path.
    :param file_path: Path to file including filename.
    :return: File size in bytes.
    """
    return os.stat(file_path).st_size
