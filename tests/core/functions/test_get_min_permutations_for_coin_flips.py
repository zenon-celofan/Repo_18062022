import pytest

from core.functions.get_min_permutations_for_coin_flips import get_min_permutations_for_coin_flips


@pytest.mark.parametrize('test_coin_flips_record, expected_returned_value', [
    ([], 0),
    ([1], 0),
    ([0, 0, 1], 1),
    ([1, 1, 0], 1),
    ([1, 0, 1], 0),
    ([0, 1, 0, 1], 0),
    ([1, 1, 0, 1, 0], 2),
    ([1, 1, 0, 1, 0, 0], 1),
    ([1, 1, 1, 0, 0, 0], 1)])
def test_get_min_permutations_for_coin_flips_proper_execution(
        test_coin_flips_record,
        expected_returned_value):
    returned_value = get_min_permutations_for_coin_flips(test_coin_flips_record)

    assert returned_value == expected_returned_value


@pytest.mark.parametrize('test_coin_flips_record', [[-1, 0], ['1', '1', '0'], [1, 2, 3]])
def test_get_min_permutations_for_coin_flips_exception_raise_typeerror(test_coin_flips_record):
    with pytest.raises(TypeError):
        get_min_permutations_for_coin_flips(test_coin_flips_record)


def test_get_min_permutations_for_coin_flips_exception_raise_valueerror():
    with pytest.raises(ValueError):
        get_min_permutations_for_coin_flips([1, 1])
