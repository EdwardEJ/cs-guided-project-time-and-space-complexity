"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # Your code here
    # variable for current index in loop
    # add to variable while looping through
    # i + j?

    # for i in range(len(nums)):
    #   for j in range(i + 1, len(nums)):
    #     if nums[i] + nums[j] == target:
    #       return [i, j]
    # return 'No match found'

  dict = {}
  
  for index, num in enumerate(nums): #0(n)
    dict[num] = index
  
  for index, num in enumerate(nums): #O(n)
    diff = target - num
    if diff in dict:
      if diff == num:
        continue
      return [index, dict[diff]]
  

    # for i in range(len(nums)):
    #   dict[nums[i]] = i

    # for i in range(len(nums)):
    #   complement = target - nums[i]
    #   if complement in dict and dict[complement] != i:
    #     return [i, dict[target - nums[i]]]
    
    return 'No solution found'

print(two_sum([2,5,9,13], 7))
print(two_sum([4, 3, 5], 8))

# Alternative solution:
# Create dictionary with array as keys and matching indices as values
#loop over list of nums to populate this dictionary
#loop over list of nums
  #check if target - nums[i] is in our dictionary
  #if it is, return the two indices

