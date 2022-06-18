import os


def is_file_owner_admin(file_path: str) -> bool:
    """
    Checks if given file is owned by 'root' (uid=0) user.
    This function works only in 'posix' environment.
    :param file_path: Path to file including filename.
    :return: True is owner of the file is root, with uid = 0,
        False otherwise.
    """
    ADMIN_UID = 0

    file_uid = os.stat(file_path).st_uid
    return file_uid == ADMIN_UID
