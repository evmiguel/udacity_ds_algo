

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    assert number > -1

    if isinstance(number, float):
        number = int(number)

    left = 0
    right = number
    while left < right:
        mid = (left + right)//2
        if mid*mid > number:
            right = mid - 1
        elif mid*mid < number:
            left = mid + 1
        else:
            return mid
    return left

# Test integers
print ("Pass" if  (3 == sqrt(9)) else "Fail") # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Pass

# Test float
print ("Pass" if  (1 == sqrt(1.1)) else "Fail") # Pass

try:
    sqrt(-1)
except AssertionError:
    pass