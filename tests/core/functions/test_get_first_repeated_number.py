import pytest

from core.exceptions import RepeatedNumberNotFound
from core.functions.get_first_repeated_number import get_first_repeated_number


@pytest.mark.parametrize('test_primary_vector, test_secondary_vector, expected_return_value', [
    ([1, 2, 3], [1, 2, 3], 1),
    ([0], [3, 0, 5], 0),
    ([-1, -2, 3], [-2, -1], -1)])
def test_get_first_repeated_number_proper_execution(
        test_primary_vector,
        test_secondary_vector,
        expected_return_value):
    returned_value = get_first_repeated_number(test_primary_vector, test_secondary_vector)

    assert returned_value == expected_return_value


def test_get_first_repeated_number_exception_raise():
    with pytest.raises(RepeatedNumberNotFound):
        get_first_repeated_number([1], [2])
