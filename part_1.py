from core.functions.find_specific_file_in_path import find_specific_file_in_path
from core.functions.get_first_repeated_number import get_first_repeated_number
from core.functions.get_min_permutations_for_coin_flips import get_min_permutations_for_coin_flips

if __name__ == '__main__':
    """
    This script is solving tasks 1-3 by using dedicated functions.
    Task 1:
        A function that given 2 vectors of integers finds 
        the first repeated number.
    Task 2:
         A function that given a path of the file system finds
         the first file that meets the following requirements:
          a. The file owner is admin
          b. The file is executable
          c. The file has a size lower than 14*2^20
    Task 3:
        A function that given a sequence of coin flips (0 is tails, 1 is heads) 
        finds the minimum quantity of permutations so that the sequence 
        ends interspersed. For example, given the sequence 0,1,1,0 how many
        changes are needed so that the result is 0,1,0,1
        """
    # Task 1
    print(get_first_repeated_number(
        primary_vector=[7, 2, 3],
        secondary_vector=[2, 3, 4, 5, 6, 7]))

    # Task 2
    print(find_specific_file_in_path('misc/my_dir/'))

    # Task 3
    print(get_min_permutations_for_coin_flips([1, 1, 1, 0, 0, 0]))
