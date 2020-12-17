from typing import List

from typing import List

def csSortedTwoSum(numbers: List[int], target: int) -> List[int]:
    dict = {}
    for index, num in enumerate(numbers): #0(n)
        dict[num] = index
    
    for index, num in enumerate(numbers):
        diff = target - num
        if diff == num:
            continue
        if diff in dict:
            return [index, dict[diff]]

print(csSortedTwoSum([3, 12, 8, 16], 11))