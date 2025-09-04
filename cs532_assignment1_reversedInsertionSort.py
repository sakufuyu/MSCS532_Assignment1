
import random


def reversed_insertion_sort(nums: list[int]) -> list[int]:
    """
    Sorts a list in descending order using the insertion sort algorithm.

    Args:
        nums: List of integers to be sorted.

    Returns:
        The sorted list (in-place sorting)
    """
    len_nums = len(nums)

    for i in range(1, len_nums):
        temp = nums[i]
        j = i - 1
        # Move elements greater than temp to one position ahead
        while (j >= 0 and nums[j] < temp):  # For descending order
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp


def reversed_insertion_sort_recursive(nums: list[int], n: int) -> list[int]:
    """
    Recursively sorts a list in descending order using insertion sort.

    Args:
        nums: List of integers to be sorted
        n: Lenght of the list to be considered

    Returns:
        The sorted list (in-place sorting)
    """
    # Base case: if array has 0 or 1 elements, it's already sorted.
    if (n <= 1):
        return

    # Sort the first n-1 elements
    reversed_insertion_sort_recursive(nums, n-1)

    # Insert the last elements at the correct position
    temp = nums[n-1]
    n -= 2

    # Move elements smaller than temp to one position ahead
    while (n >= 0 and nums[n] < temp):
        nums[n+1] = nums[n]
        n -= 1
    nums[n+1] = temp


def generate_random_list(size: int) -> list[int]:
    """
    Generates a list of random integers.

    Args:
        size: The number of random integers to generate.

    Returns:
        A list of random integers.
    """
    return [random.randint(0, 100) for _ in range(size)]


if __name__ == "__main__":
    list_1 = generate_random_list(10)
    print(list_1)
    reversed_insertion_sort(list_1)
    print(list_1)

    list_2 = generate_random_list(20)
    print(list_2)
    reversed_insertion_sort_recursive(list_2, len(list_2))
    print(list_2)
