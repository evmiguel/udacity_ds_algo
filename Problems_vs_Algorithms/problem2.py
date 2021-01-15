def find_pivot_point(input_list):
    left = 0
    right = len(input_list) - 1
    
    while left <= right:
        mid = (left + right)//2
        if mid == 0 or input_list[mid] < input_list[mid - 1]:
            return mid
        if input_list[mid] > input_list[0]:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

def binary_search(input_list, number, left, right):
    while left <= right:
        mid = (left + right)//2
        if number > input_list[mid]:
            left = mid + 1
        elif number < input_list[mid]:
            right = mid - 1
        else:
            return mid
    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    assert isinstance(number, int)
    
    pivot_point = find_pivot_point(input_list)

    if pivot_point == 0 or number < input_list[0]:
        return binary_search(input_list, number, pivot_point, len(input_list) - 1)
    
    return binary_search(input_list, number, 0, pivot_point-1)
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Pass

# Test number not in the array
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Pass

# Test empty array
test_function([[], 10]) # Pass

# Test target that is not a number
try:
    rotated_array_search([6, 7, 8, 1, 2, 3, 4], None)
except AssertionError:
    pass
