def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    if number == None or number == '' or number < 0:
        return 'invalid input'

    first = 1
    last = number // 2

    while last >= first:
        mid = (last + first) // 2
        if mid * mid == number:
            return mid
        elif mid * mid > number:
            last = mid - 1
        elif mid * mid < number:
            first = mid + 1
            result = mid
    return result


def test(num, result):
    if sqrt(num) == result:
        print("Pass: Square Root of {} equals to {}".format(
            num, result))
    else:
        print("Fail: Expected Result: {} Vs: {}".format(
            result, sqrt(num)))

# Pass
test(9, 3)  
test(1, 1)  
test(27, 5) 
test(30, 5) 
test(-2, 'invalid input')  
test(None, 'invalid input')
