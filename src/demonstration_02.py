"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 1
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
  #how could we save data to write an implementation that is more efficient?
  #for any given number, we'd like to know if we've seen this number already
  #can we somehow save each number we've seen in such a way that when we see the nextcopy of it

  #loop through nums
    #check if the num is in our set
    #if it is
      #remove it from our set
    #if it isnt
      #add it to the set
    
  #the only thing left in the set should be the odd-number-out
  s = set()

  for num in nums: #O(n)
    if num in s: #O(1)
      s.remove(num) #O(1)
    else:
      s.add(num) #O(1)

  return list(s)[0]