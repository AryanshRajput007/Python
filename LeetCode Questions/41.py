class Solution(object):
  def firstMissingPositive(self, nums):
      nums.append(0)  # Add 0 to the list to handle the case where the first missing positive integer is 1
      n = len(nums)
      for i in range(len(nums)):  # Replace negative numbers and numbers greater than n with 0
          if nums[i] < 0 or nums[i] >= n:
              nums[i] = 0
      for i in range(len(nums)):  # Use the list indices as hash keys and mark the presence of a number by negating the number at that index
          nums[nums[i] % n] += n
      for i in range(1, len(nums)):
          if nums[i] < n:  # The first index with a non-positive number indicates the first missing positive integer
              return i
      return n  # If all positive integers from 1 to n are present, the first missing positive integer is n+1
