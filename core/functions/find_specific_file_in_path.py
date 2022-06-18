import os
from typing import Optional

from core.functions.get_file_size import get_file_size
from core.functions.is_file_executable import is_file_executable
from core.functions.is_file_owner_admin import is_file_owner_admin


def find_specific_file_in_path(directory_path: str) -> Optional[str]:
    """
    Functions returns first file found in given directory path,
        which meets requirements:
     - owner of the file is 'root' (uid=0)
     - file is executable
     - file size is less than 14 * 2^20 bytes.
    :param directory_path: Path to directory with files to search.
    :return: Filename of the file that meets the requirements
        or None is such file is not found.
    """
    max_file_size = 14 * 2 ** 20

    files_list = os.listdir(directory_path)
    for filename in files_list:
        file_path = os.path.join(directory_path, filename)

        if all([
                is_file_executable(file_path),
                is_file_owner_admin(file_path),
                get_file_size(file_path) < max_file_size]):
            return filename

    return None
