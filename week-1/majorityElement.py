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
