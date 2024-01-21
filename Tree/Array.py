class Solution:
  # Boyer-Moore majority vote
  def majorityNumber(self, nums):
    majority = nums[0]
    counter = 0
    for num in nums:
      if counter == 0:
        majority = num
        counter = counter + 1
      elif num == majority:
        counter = counter + 1
      else:
        counter = counter - 1
    return majority