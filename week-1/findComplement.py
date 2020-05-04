# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    comp = {'0': '1', '1': '0'}
    binNum = str(bin(num)[2:])
    return int(''.join(comp[x] for x in binNum), 2)
