
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


def main():
    # Flag to control the main application loop
    is_continue = True
    print("### Reversed Insertion Sort application ###")

    while (is_continue):
        # Get user input for list size
        print("Select your preferred list size: => ", end="")
        try:
            list_size = int(input())
            if (list_size <= 0):
                raise ValueError("List size must be a positive integer.")
        except ValueError as e:
            print(f"Invalid input. Please enter a valid integer. {e}")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        # Generate a random list of integers based on user input
        nums = generate_random_list(list_size)
        print(f"Unsorted list generated: {nums}")
        print()

        # Display sorting options to the user
        print("Select your preferred sorting implementation approach:")
        print("    1. Iterative")
        print("    2. Recursive")
        print("    Select any other key to Exit")
        print("=> ", end="")
        user_input = input()

        # Process user's choice
        if (user_input == "1"):
            reversed_insertion_sort(nums)
            print(f"Sorted list: {nums}")
        elif (user_input == "2"):
            reversed_insertion_sort_recursive(nums, len(nums))
            print(f"Sorted list: {nums}")
        else:
            print("Exiting the application...")
            is_continue = False
        print("\n\n#####################################################\n")


# Entry point of the program
if __name__ == "__main__":
    main()
