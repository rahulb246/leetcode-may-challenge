# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

def firstUniqChar(s):
      """
      :type s: str
      :rtype: int
      """
      dup = {}
      for c in s:
          if c in dup:
              dup[c] += 1
          else:
              dup[c] = 1

      for idx, c in enumerate(s):
          if dup[c] == 1:
              return idx

      return -1
