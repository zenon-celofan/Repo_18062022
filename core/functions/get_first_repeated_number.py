from typing import List

from core.exceptions import RepeatedNumberNotFound


def get_first_repeated_number(primary_vector: List[int], secondary_vector: List[int]) -> int:
    """
    Function returns first item from primary_vector found in secondary_vector.
    :param primary_vector: Primary vestor - list of integers.
    :param secondary_vector: Secondary vector - list of integers.
    :return: First integer in primary_vector found in secondary_vector.
    """
    for number in primary_vector:
        if number in secondary_vector:
            return number
    raise RepeatedNumberNotFound('No repeated numbers found in given vectors.')
