from unittest.mock import Mock, patch

import pytest

from core.functions.is_file_owner_admin import is_file_owner_admin


@pytest.mark.parametrize('mocked_file_uid, expected_returned_value', [
    (0, True),
    (Mock(), False)])
@patch('core.functions.is_file_owner_admin.os')
def test_is_file_owner_admin(
        mocked_os,
        mocked_file_uid,
        expected_returned_value):
    mocked_os.stat().st_uid = mocked_file_uid
    mocked_file_patch = Mock()

    returned_value = is_file_owner_admin(mocked_file_patch)

    assert returned_value == expected_returned_value
