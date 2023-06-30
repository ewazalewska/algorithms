# Binary search algorithm implementation

def binary_search(searched, numbers):
    """
    Perform binary search to find if target element is in the sorted array.

    Args:
        numbers (list): The sorted array to search in.
        searched: The element to search for.

    Returns:
        str: Message if list contains number.
    """

    left = 0                        # Leftmost index of the sublist
    right = len(numbers) - 1        # Rightmost index of the sublist

    while left <= right:
        middle = (right + left) // 2    # Middle index of the sublist

        if searched == numbers[middle]:
            print(f"Number {searched} is on the list")
            break

        elif searched < numbers[middle]:        # If searched number is smaller, update right index and search in the "left part"
            right = middle - 1

        else:
            left = middle + 1                   # If searched number is larger, update left index and search in the "right part"

    else:
        print(f"Number {searched} not found.")

# Example of use

sorted_list = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500, 501]
number = 34

binary_search(number, sorted_list)