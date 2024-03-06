

def recursive_search(arr, target, index=0):
    """
    Recursive function to search for a target value in a list.

    :param arr: List of numbers to search within.
    :param target: The number to search for.
    :param index: The current index in the list (starts from 0).
    :return: The index of the target if found, otherwise a message indicating it's not in the list.
    """
    # Base case: If the end of the list is reached without finding the target
    if index == len(arr):
        return "The target is not in the list."

    # If the target is found at the current index
    if arr[index] == target:
        return f"Target found at index {index}"

    # Recursive case: Move to the next index
    return recursive_search(arr, target, index + 1)

if __name__ == "__main__":
    numbers_list = [5, 3, 7, 1, 2, 8, 4]
    target_number = int(input("Enter the number to search for: "))
    result = recursive_search(numbers_list, target_number)
    print(result)
