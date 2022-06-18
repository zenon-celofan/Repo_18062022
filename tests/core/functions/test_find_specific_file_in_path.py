from unittest.mock import patch, Mock

from core.functions.find_specific_file_in_path import find_specific_file_in_path


@patch('core.functions.find_specific_file_in_path.get_file_size')
@patch('core.functions.find_specific_file_in_path.is_file_owner_admin')
@patch('core.functions.find_specific_file_in_path.is_file_executable')
@patch('core.functions.find_specific_file_in_path.os')
def test_find_specific_file_in_path_with_file_found(
        mocked_os,
        is_file_executable,
        is_file_owner_admin,
        get_file_size):
    mocked_os.listdir.return_value = ['mocked_filename_1', 'mocked_filename_2', 'mocked_filename_3']
    is_file_executable.side_effect = [False, True, True]
    is_file_owner_admin.side_effect = [False, False, True]
    get_file_size.side_effect = [0, 20e6, 10e6]

    returned_value = find_specific_file_in_path(Mock())

    assert returned_value == 'mocked_filename_3'


@patch('core.functions.find_specific_file_in_path.get_file_size')
@patch('core.functions.find_specific_file_in_path.is_file_owner_admin')
@patch('core.functions.find_specific_file_in_path.is_file_executable')
@patch('core.functions.find_specific_file_in_path.os')
def test_find_specific_file_in_path_with_file_not_found(
        mocked_os,
        is_file_executable,
        is_file_owner_admin,
        get_file_size):
    mocked_os.listdir.return_value = ['mocked_filename_1']
    is_file_executable.side_effect = [True]
    is_file_owner_admin.side_effect = [True]
    get_file_size.side_effect = [50e6]

    returned_value = find_specific_file_in_path(Mock())

    assert returned_value is None
