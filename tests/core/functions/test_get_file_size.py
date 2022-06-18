from unittest.mock import Mock, patch

from core.functions.get_file_size import get_file_size


@patch('core.functions.get_file_size.os')
def test_get_file_size(mocked_os):
    mocked_file_patch = Mock()

    returned_value = get_file_size(mocked_file_patch)

    mocked_os.stat.assert_called_once_with(mocked_file_patch)

    assert returned_value == mocked_os.stat().st_size
