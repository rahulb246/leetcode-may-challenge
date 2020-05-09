# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

def majorityElement(nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      d = {}
      for n in nums:
          if n in d:
              d[n] += 1
          else:
              d[n] = 1

      for i in d:
          if d[i] > len(nums) // 2:
              return i
