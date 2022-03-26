def sum13(nums):
  c = 0
  for i in range(len(nums)):
    if(nums[i] != 13):
      if(i > 0 and nums[i-1] != 13): c += nums[i]
      if(i == 0): c += nums[i]
      
  return c
