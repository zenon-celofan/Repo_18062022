from typing import List


def get_min_permutations_for_coin_flips(coin_flips_record: List[int]) -> int:
    """
    Function calculates the minimum number of permutations
        (swaps of pair of elements) of given coin flips record
        needed to create interspersed list.
    :param coin_flips_record: List of consecutive coin flips results:
        0 - 'tails',
        1 - 'heads'.
    :return: Calculated minimum number of permutations.
    """
    flips_record_str = ''.join(map(str, coin_flips_record))

    if flips_record_str.translate({
            ord('0'): None,
            ord('1'): None}):
        raise TypeError('Input vectors must contain only 0 and 1.')

    if '11' not in flips_record_str and '00' not in flips_record_str:
        return 0

    if abs(coin_flips_record.count(0) - coin_flips_record.count(1)) > 1:
        raise ValueError('Given coin flips record can\'t be translated to interspersed list')

    interspersed_record = [x % 2 for x in range(len(coin_flips_record))]

    changes = []
    for item_1, item_2 in zip(coin_flips_record, interspersed_record):
        changes.append(item_1 - item_2)

    if len(coin_flips_record) % 2 == 0:
        return min(changes.count(1), changes.count(0) // 2)
    else:
        return max(changes.count(1), changes.count(0) // 2)
