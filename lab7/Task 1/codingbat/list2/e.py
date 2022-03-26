from operator import truediv


def sum67(nums):
  sum = 0
  isBetween = False
  for i in range(len(nums)):
    if(nums[i] == 6):
      isBetween = True
    if not isBetween:
      sum += nums[i]
    if nums[i] is 7 and isBetween:
      isBetween = False
  return sum