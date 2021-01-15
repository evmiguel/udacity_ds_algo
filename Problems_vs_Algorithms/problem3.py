def mergesort_descending(items):
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort_descending(left)
    right = mergesort_descending(right)
    
    return merge(left, right)
    
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    descending_list = mergesort_descending(input_list)
    update = 0
    multiplier = 1
    max_sum = [0,0]
    for i, item in enumerate(descending_list):
        if i > 0 and i % 2 == 0:
            multiplier = 10
        max_sum[update] = max_sum[update]*multiplier + item
        update = not update
    return max_sum

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test 2 elements
test_function([[1, 100], [100, 1]])

# Test 1 element
test_function([[1], [1, 0]])

# Test 0 elements
test_function([[], [0, 0]])
