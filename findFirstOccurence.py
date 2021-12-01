# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

# Input:

# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output:

# 1
# Explanation: First occurrence of 3 is at index 1.


from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    current = 0
    while (current < len(arr)):
      if(arr[current] == target): 
        return current
      else:
        current += 1 
      
    return -1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)


arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3

output = find_first_occurrence(arr, target)
print(output)
