# MSCS532_Assignment1
## Fuyuki Kobayashi

# Reversed Insertion Sort

This Python application demonstrates the implementation of insertion sort in descending order using both iterative and recursive approaches.

## Overview

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. The algorithm works by taking one element from the unsorted portion of the array and inserting it into its correct position in the sorted portion of the array.

This implementation specifically sorts arrays in descending order (from highest to lowest).

## Features

- **Two sorting implementations**:
  - Iterative approach
  - Recursive approach
- **Random list generation**: Creates lists of integers with user-specified size
- **Interactive CLI**: User-friendly command-line interface

## Usage

1. Run the script:
   ```
   python reversed_insertion_sort.py
   ```

2. Enter the desired list size when prompted.

3. Choose a sorting implementation:
   - Option 1: Iterative approach
   - Option 2: Recursive approach
   - Any other key: Exit the application

## Functions

### `reversed_insertion_sort(nums: list[int]) -> list[int]`

Sorts a list in descending order using the iterative insertion sort algorithm.

### `reversed_insertion_sort_recursive(nums: list[int], n: int) -> list[int]`

Sorts a list in descending order using the recursive insertion sort algorithm.

### `generate_random_list(size: int) -> list[int]`

Generates a list of random integers between 0 and 100.

## Example output

```
### Reversed Insertion Sort application ###
Select your preferred list size: => 5
Unsorted list generated: [42, 23, 87, 15, 61]

Select your preferred sorting implementation approach:
    1. Iterative
    2. Recursive
    Select any other key to Exit
=> 1
Sorted list: [87, 61, 42, 23, 15]


#####################################################
```

## Requirements

- Python 3.x
- No external libraries required

## Notes

- Both sorting functions modify the input list in-place.
- Time complexity: O(n²) for both implementations.
- Space complexity: O(1) for the iterative version, O(n) for the recursive version due to the call stack.