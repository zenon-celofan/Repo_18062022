from unittest.mock import Mock, patch

import pytest

from core.functions.is_file_executable import is_file_executable


@pytest.mark.parametrize(
    'mocked_isfile_return_value, mocked_access_return_value, expected_return_value', [
        (False, False, False),
        (True, False, False),
        (False, True, False),
        (True, True, True)])
@patch('core.functions.is_file_executable.os')
def test_is_file_executable(
        mocked_os,
        mocked_isfile_return_value,
        mocked_access_return_value,
        expected_return_value):
    mocked_os.path.isfile.return_value = mocked_isfile_return_value
    mocked_os.access.return_value = mocked_access_return_value
    mocked_file_patch = Mock()

    returned_value = is_file_executable(mocked_file_patch)

    mocked_os.path.isfile.assert_called_once_with(mocked_file_patch)
    mocked_os.access.assert_called_once_with(mocked_file_patch, mocked_os.X_OK)

    assert returned_value == expected_return_value
