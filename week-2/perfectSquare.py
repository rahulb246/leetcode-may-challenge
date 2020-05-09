# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.

def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    i = 1
    while i*i <= num: 
        if ((num % i == 0) and (num / i == i)): 
            return True
        i += 1
    return False
