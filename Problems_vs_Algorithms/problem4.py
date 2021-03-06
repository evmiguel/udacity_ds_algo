def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pos_0 = 0
    pos_2 = len(input_list)-1
    left = 0
    
    while left <= pos_2:
        assert isinstance(input_list[left], int) and input_list[left] >= 0 and input_list[left] <= 2
        if input_list[left] == 0:
            input_list[left] = input_list[pos_0]
            input_list[pos_0] = 0
            pos_0 += 1
            left += 1
        elif input_list[left] == 2:
            input_list[left] = input_list[pos_2]
            input_list[pos_2] = 2
            pos_2 -= 1
        else:
            left += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test empty array
test_function([])

# Test number not 0, 1, or 2
try:
    test_function([3,0,1])
except AssertionError:
    pass